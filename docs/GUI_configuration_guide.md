# GUI Domain AWS Settings Guide

## Platform Deployment
Currently, GUI tasks are only supported on the AWS platform.  
Our AWS setup closely follows the OSWorld public evaluation guide, and we sincerely thank the OSWorld team for their detailed documentation and infrastructure design. We also use the AMI provided by X-Lang Lab in the OSWorld project.

### Step 1: Launch the Host Instance (optional but recommended)
1. In the AWS Console, create an EC2 instance. We recommend instance type **`t3.large`** or a higher‑performance instance as the host machine.
2. **Storage**: 50 GB is recommended.
3. **Security group**: Optionally open port 8080 for the monitoring service.
4. **VPC**: Use the default VPC (note the VPC ID for later use).
5. (Optional) The default vCPU limit for T-family instances is 16. We recommend requesting a limit increase to 32 vCPUs to speed up evaluation.

### Step 2: Connect to Host Instance

1. Download the `.pem` key file when creating the instance
2. Set permissions:
   ```bash
   chmod 400 <your_key_file_path>
   ```
3. Connect via SSH:
   ```bash
   ssh -i <your_key_path> ubuntu@<your_public_dns>
   ```

### Step 3: Set Up Host Machine

```bash
# Clone AJ-Bench repository
git clone git@github.com:aj-bench/AJ-Bench.git
cd AJ-Bench

# Optional: create a Conda environment
# conda create -n aj-bench python=3.11
# conda activate aj-bench

# Install core dependencies
pip install -e .

# If you only need GUI domain evaluation, you can run the following command instead
# pip install -r requirements_gui.txt
```

### Step 4: Configure AWS Client Machines

For the AWS client instances, we recommend using instance type **`t3-medium`**.  

#### Security Group Configuration

Create a security group with the following rules:

**Inbound Rules** (8 rules required):

| Type       | Protocol | Port Range | Source         | Description                |
|------------|----------|------------|----------------|----------------------------|
| SSH        | TCP      | 22         | 0.0.0.0/0      | SSH access                 |
| HTTP       | TCP      | 80         | 172.31.0.0/16  | HTTP traffic               |
| Custom TCP | TCP      | 5000       | 172.31.0.0/16  | OSWorld backend service    |
| Custom TCP | TCP      | 5910       | 0.0.0.0/0      | NoVNC visualization port   |
| Custom TCP | TCP      | 8006       | 172.31.0.0/16  | VNC service port           |
| Custom TCP | TCP      | 8080       | 172.31.0.0/16  | VLC service port           |
| Custom TCP | TCP      | 8081       | 172.31.0.0/16  | Additional service port    |
| Custom TCP | TCP      | 9222       | 172.31.0.0/16  | Chrome control port        |

**Outbound Rules** (1 rule required):

| Type        | Protocol | Port Range | Destination | Description                 |
|-------------|----------|------------|-------------|----------------------------|
| All traffic | All      | All        | 0.0.0.0/0   | Allow all outbound traffic |

Record the `AWS_SECURITY_GROUP_ID`.

#### VPC and Subnet Configuration

1. Note the **VPC ID** and **Subnet ID** from your host instance
2. Record the **Subnet ID** as `AWS_SUBNET_ID`

#### AWS Access Keys

1. Go to AWS Console → Security Credentials
2. Create access key
3. Record `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`

## Environment Setup

### Set Environment Variables

```bash

export OPENAI_API_KEY="your_openai_api_key"
export DEEPSEEK_API_KEY="your_deepseek_api_key"

# AWS Configuration
export AWS_ACCESS_KEY_ID="your_access_key"
export AWS_SECRET_ACCESS_KEY="your_security_access_key"
export AWS_REGION="us-east-1" # Depend on the ami we used
export AWS_SECURITY_GROUP_ID="sg-xxxx"
export AWS_SUBNET_ID="subnet-xxxx"

# Or you can write them in .mcp_env file
```