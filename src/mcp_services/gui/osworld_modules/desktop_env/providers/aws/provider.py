import boto3
from botocore.exceptions import ClientError

import logging
import os
import time
import requests
from datetime import datetime, timedelta, timezone
from ..base import Provider

# TTL configuration
from .config import ENABLE_TTL, DEFAULT_TTL_MINUTES, AWS_SCHEDULER_ROLE_ARN
from .scheduler_utils import schedule_instance_termination

logger = logging.getLogger("desktopenv.providers.aws.AWSProvider")
logger.setLevel(logging.INFO)

WAIT_DELAY = 15
MAX_ATTEMPTS = 10


def _is_running_on_aws() -> bool:
    """
    检测客户端是否在 AWS EC2 实例上运行
    通过尝试访问 EC2 实例元数据服务来判断
    """
    try:
        # EC2 实例元数据服务的 URL（仅在 EC2 实例内部可访问）
        response = requests.get(
            "http://169.254.169.254/latest/meta-data/instance-id",
            timeout=1
        )
        return response.status_code == 200
    except Exception:
        return False


class AWSProvider(Provider):


    def start_emulator(self, path_to_vm: str, headless: bool, *args, **kwargs):
        logger.info("Starting AWS VM...")
        ec2_client = boto3.client('ec2', region_name=self.region)

        try:
            # Check the current state of the instance
            response = ec2_client.describe_instances(InstanceIds=[path_to_vm])
            state = response['Reservations'][0]['Instances'][0]['State']['Name']
            logger.info(f"Instance {path_to_vm} current state: {state}")

            if state == 'running':
                # If the instance is already running, skip starting it
                logger.info(f"Instance {path_to_vm} is already running. Skipping start.")
                return

            if state == 'stopped':
                # Start the instance if it's currently stopped
                ec2_client.start_instances(InstanceIds=[path_to_vm])
                logger.info(f"Instance {path_to_vm} is starting...")

                # Wait until the instance reaches 'running' state
                waiter = ec2_client.get_waiter('instance_running')
                waiter.wait(
                    InstanceIds=[path_to_vm],
                    WaiterConfig={'Delay': WAIT_DELAY, 'MaxAttempts': MAX_ATTEMPTS}
                )
                logger.info(f"Instance {path_to_vm} is now running.")
            else:
                # For all other states (terminated, pending, etc.), log a warning
                logger.warning(f"Instance {path_to_vm} is in state '{state}' and cannot be started.")

        except ClientError as e:
            logger.error(f"Failed to start the AWS VM {path_to_vm}: {str(e)}")
            raise


    def get_ip_address(self, path_to_vm: str) -> str:
        logger.info("Getting AWS VM IP address...")
        ec2_client = boto3.client('ec2', region_name=self.region)

        try:
            response = ec2_client.describe_instances(InstanceIds=[path_to_vm])
            for reservation in response['Reservations']:
                for instance in reservation['Instances']:
                    private_ip_address = instance.get('PrivateIpAddress', '')
                    public_ip_address = instance.get('PublicIpAddress', '')
                    
                    # 决定使用哪个 IP 地址
                    # 1. 优先检查环境变量 AWS_USE_PUBLIC_IP（显式配置）
                    use_public_ip_env = os.getenv('AWS_USE_PUBLIC_IP', '').lower()
                    if use_public_ip_env in {'1', 'true', 'yes', 'on'}:
                        use_public_ip = True
                        logger.info("🔧 Using public IP (AWS_USE_PUBLIC_IP=true)")
                    elif use_public_ip_env in {'0', 'false', 'no', 'off'}:
                        use_public_ip = False
                        logger.info("🔧 Using private IP (AWS_USE_PUBLIC_IP=false)")
                    else:
                        # 2. 自动检测：如果客户端不在 AWS 上运行，使用公网 IP
                        is_on_aws = _is_running_on_aws()
                        use_public_ip = not is_on_aws
                        if is_on_aws:
                            logger.info("🔧 Detected: Running on AWS EC2, using private IP")
                        else:
                            logger.info("🔧 Detected: Running locally, using public IP")
                    
                    # 选择要使用的 IP
                    if use_public_ip:
                        if public_ip_address:
                            ip_to_use = public_ip_address
                            logger.info(f"✅ Selected public IP: {public_ip_address}")
                        else:
                            logger.warning("⚠️ Public IP not available, falling back to private IP")
                            ip_to_use = private_ip_address
                    else:
                        if private_ip_address:
                            ip_to_use = private_ip_address
                            logger.info(f"✅ Selected private IP: {private_ip_address}")
                        else:
                            logger.warning("⚠️ Private IP not available, falling back to public IP")
                            ip_to_use = public_ip_address
                    
                    # 显示 VNC URL（如果有公网 IP）
                    if public_ip_address:
                        vnc_url = f"http://{public_ip_address}:5910/vnc.html"
                        logger.info("="*80)
                        logger.info(f"🖥️  VNC Web Access URL: {vnc_url}")
                        logger.info(f"📡 Public IP: {public_ip_address}")
                        logger.info(f"🏠 Private IP: {private_ip_address}")
                        logger.info(f"🔧 Using IP: {ip_to_use} ({'Public' if ip_to_use == public_ip_address else 'Private'})")
                        logger.info("="*80)
                        print(f"\n🌐 VNC Web Access URL: {vnc_url}")
                        print(f"📍 Please open the above address in the browser for remote desktop access\n")
                    else:
                        logger.warning("No public IP address available for VNC access")
                        logger.info(f"🔧 Using IP: {ip_to_use} (Private)")
                    
                    return ip_to_use
            return ''  # Return an empty string if no IP address is found
        except ClientError as e:
            logger.error(f"Failed to retrieve IP address for the instance {path_to_vm}: {str(e)}")
            raise

    def save_state(self, path_to_vm: str, snapshot_name: str):
        logger.info("Saving AWS VM state...")
        ec2_client = boto3.client('ec2', region_name=self.region)

        try:
            image_response = ec2_client.create_image(InstanceId=path_to_vm, Name=snapshot_name)
            image_id = image_response['ImageId']
            logger.info(f"AMI {image_id} created successfully from instance {path_to_vm}.")
            return image_id
        except ClientError as e:
            logger.error(f"Failed to create AMI from the instance {path_to_vm}: {str(e)}")
            raise

    def _resolve_snapshot_to_ami(self, snapshot_name: str) -> str:
        """
        Resolve snapshot name to actual AMI ID.
        For AWS, snapshots are stored as AMIs, so we need to:
        1. If snapshot_name is already an AMI ID (ami-xxx), return it directly
        2. If it's a logical name like 'init_state', look up the corresponding AMI
        3. Fall back to the default AMI from IMAGE_ID_MAP if available
        """
        # Import here to avoid circular imports
        from .manager import IMAGE_ID_MAP
        
        # If it's already an AMI ID, return it directly
        if snapshot_name.startswith('ami-'):
            return snapshot_name
            
        # For logical names like 'init_state', use the default AMI from IMAGE_ID_MAP
        if self.region in IMAGE_ID_MAP:
            # For now, use the default screen size (1920, 1080)
            # TODO: Make screen size configurable
            screen_size = (1920, 1080)
            if screen_size in IMAGE_ID_MAP[self.region]:
                ami_id = IMAGE_ID_MAP[self.region][screen_size]
                logger.info(f"Using default AMI for region {self.region}: {ami_id}")
                return ami_id
        
        # If we can't resolve it, raise an error
        raise ValueError(f"Cannot resolve snapshot name '{snapshot_name}' to AMI ID. "
                        f"Region: {self.region}, Available regions: {list(IMAGE_ID_MAP.keys())}")

    def revert_to_snapshot(self, path_to_vm: str, snapshot_name: str):
        logger.info(f"Reverting AWS VM to snapshot AMI: {snapshot_name}...")
        ec2_client = boto3.client('ec2', region_name=self.region)

        try:
            # Step 1: Retrieve the original instance details
            instance_details = ec2_client.describe_instances(InstanceIds=[path_to_vm])
            instance = instance_details['Reservations'][0]['Instances'][0]
            security_groups = [sg['GroupId'] for sg in instance['SecurityGroups']]
            subnet_id = instance['SubnetId']
            instance_type = instance['InstanceType']
            
            # Step 2: Terminate the old instance
            ec2_client.terminate_instances(InstanceIds=[path_to_vm])
            logger.info(f"Old instance {path_to_vm} has been terminated.")

            # Step 3: Resolve snapshot name to actual AMI ID
            ami_id = self._resolve_snapshot_to_ami(snapshot_name)
            logger.info(f"Resolved snapshot '{snapshot_name}' to AMI ID: {ami_id}")

            # Step 4: Launch a new instance from the snapshot(AMI) with performance optimization
            logger.info(f"Launching a new instance from AMI {ami_id}...")
            
            # TTL configuration follows the same env flags as allocation (centralized)
            enable_ttl = ENABLE_TTL
            default_ttl_minutes = DEFAULT_TTL_MINUTES
            ttl_seconds = max(0, default_ttl_minutes * 60)

            run_instances_params = {
                "MaxCount": 1,
                "MinCount": 1,
                "ImageId": ami_id,
                "InstanceType": instance_type,
                "EbsOptimized": True,
                "InstanceInitiatedShutdownBehavior": "terminate",
                "NetworkInterfaces": [
                    {
                        "SubnetId": subnet_id,
                        "AssociatePublicIpAddress": True,
                        "DeviceIndex": 0,
                        "Groups": security_groups
                    }
                ],
                "BlockDeviceMappings": [
                    {
                        "DeviceName": "/dev/sda1", 
                        "Ebs": {
                            # "VolumeInitializationRate": 300
                            "VolumeSize": 30,  # Size in GB
                            "VolumeType": "gp3",  # General Purpose SSD
                            "Throughput": 1000,
                            "Iops": 4000  # Adjust IOPS as needed
                        }
                    }
                ]
            }
            
            new_instance = ec2_client.run_instances(**run_instances_params)
            new_instance_id = new_instance['Instances'][0]['InstanceId']
            logger.info(f"New instance {new_instance_id} launched from AMI {snapshot_name}.")
            logger.info(f"Waiting for instance {new_instance_id} to be running...")
            ec2_client.get_waiter('instance_running').wait(InstanceIds=[new_instance_id])

            logger.info(f"Instance {new_instance_id} is ready.")
            # Schedule cloud-side termination via EventBridge Scheduler (auto-resolve role ARN)
            try:
                if enable_ttl:
                    schedule_instance_termination(self.region, new_instance_id, ttl_seconds, AWS_SCHEDULER_ROLE_ARN, logger)
            except Exception as e:
                logger.warning(f"Failed to create EventBridge Scheduler for {new_instance_id}: {e}")

            # Schedule cloud-side termination via EventBridge Scheduler (same as allocation path)
            try:
                if enable_ttl and os.getenv('AWS_SCHEDULER_ROLE_ARN'):
                    scheduler_client = boto3.client('scheduler', region_name=self.region)
                    schedule_name = f"osworld-ttl-{new_instance_id}-{int(time.time())}"
                    eta_scheduler = datetime.now(timezone.utc) + timedelta(seconds=ttl_seconds)
                    schedule_expression = f"at({eta_scheduler.strftime('%Y-%m-%dT%H:%M:%S')})"
                    target_arn = "arn:aws:scheduler:::aws-sdk:ec2:terminateInstances"
                    input_payload = '{"InstanceIds":["' + new_instance_id + '"]}'
                    scheduler_client.create_schedule(
                        Name=schedule_name,
                        ScheduleExpression=schedule_expression,
                        FlexibleTimeWindow={"Mode": "OFF"},
                        Target={
                            "Arn": target_arn,
                            "RoleArn": os.getenv('AWS_SCHEDULER_ROLE_ARN'),
                            "Input": input_payload
                        },
                        State='ENABLED',
                        Description=f"OSWorld TTL terminate for {new_instance_id}"
                    )
                    logger.info(f"Scheduled EC2 termination via EventBridge Scheduler for snapshot revert: name={schedule_name}, when={eta_scheduler.isoformat()} (UTC)")
                else:
                    logger.info("TTL enabled but AWS_SCHEDULER_ROLE_ARN not set; skipping scheduler for snapshot revert.")
            except Exception as e:
                logger.warning(f"Failed to create EventBridge Scheduler for {new_instance_id}: {e}")

            try:
                instance_details = ec2_client.describe_instances(InstanceIds=[new_instance_id])
                instance = instance_details['Reservations'][0]['Instances'][0]
                public_ip = instance.get('PublicIpAddress', '')
                if public_ip:
                    vnc_url = f"http://{public_ip}:5910/vnc.html"
                    logger.info("="*80)
                    logger.info(f"🖥️  New Instance VNC Web Access URL: {vnc_url}")
                    logger.info(f"📡 Public IP: {public_ip}")
                    logger.info(f"🆔 New Instance ID: {new_instance_id}")
                    logger.info("="*80)
                    print(f"\n🌐 New Instance VNC Web Access URL: {vnc_url}")
                    print(f"📍 Please open the above address in the browser for remote desktop access\n")
            except Exception as e:
                logger.warning(f"Failed to get VNC address for new instance {new_instance_id}: {e}")

            return new_instance_id

        except ClientError as e:
            logger.error(f"Failed to revert to snapshot {snapshot_name} for the instance {path_to_vm}: {str(e)}")
            raise


    def stop_emulator(self, path_to_vm, region=None):
        logger.info(f"Stopping AWS VM {path_to_vm}...")
        ec2_client = boto3.client('ec2', region_name=self.region)

        try:
            ec2_client.terminate_instances(InstanceIds=[path_to_vm])
            logger.info(f"Instance {path_to_vm} has been terminated.")
        except ClientError as e:
            logger.error(f"Failed to stop the AWS VM {path_to_vm}: {str(e)}")
            raise
