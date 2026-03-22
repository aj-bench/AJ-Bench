"""
Verification script for PostgreSQL Task 5: Database Schema and Data Operations
"""

import os
import sys
import psycopg2
from decimal import Decimal


def rows_match(actual_row, expected_row):
    """
    Compare two rows with appropriate tolerance.
    For Decimal types: allows 0.1 tolerance
    For date types: convert to string for comparison
    For other types: requires exact match
    """
    if len(actual_row) != len(expected_row):
        return False

    for actual, expected in zip(actual_row, expected_row):
        if isinstance(actual, Decimal) and isinstance(expected, (Decimal, float, int)):
            if abs(float(actual) - float(expected)) > 0.1:
                return False
        elif hasattr(actual, "strftime"):  # datetime.date or datetime.datetime
            if str(actual) != str(expected):
                return False
        elif actual != expected:
            return False

    return True


def get_connection_params() -> dict:
    """Get database connection parameters."""
    return {
        "host": os.getenv("POSTGRES_HOST", "localhost"),
        "port": int(os.getenv("POSTGRES_PORT", 5432)),
        "database": os.getenv("POSTGRES_DATABASE"),
        "user": os.getenv("POSTGRES_USERNAME"),
        "password": os.getenv("POSTGRES_PASSWORD"),
    }


def verify_table_structures(conn) -> bool:
    """Verify that all three tables were created with correct structure."""
    with conn.cursor() as cur:
        # Check if tables exist
        cur.execute("""
            SELECT table_name FROM information_schema.tables
            WHERE table_schema = 'employees'
            AND table_name IN ('employee_projects', 'project_assignments', 'project_milestones')
            ORDER BY table_name
        """)
        tables = [row[0] for row in cur.fetchall()]

        if len(tables) != 3:
            print(f"❌ Expected 3 tables, found {len(tables)}: {tables}")
            return False

        # Check foreign key constraints exist
        cur.execute("""
            SELECT COUNT(*) FROM information_schema.table_constraints
            WHERE table_schema = 'employees'
            AND constraint_type = 'FOREIGN KEY'
            AND table_name IN ('project_assignments', 'project_milestones')
        """)
        fkey_count = cur.fetchone()[0]

        if fkey_count != 3:
            print(f"❌ Expected 3 foreign key constraints, found {fkey_count}")
            return False

        # Check if priority column exists (added in step 6)
        cur.execute("""
            SELECT COUNT(*) FROM information_schema.columns
            WHERE table_schema = 'employees' AND table_name = 'employee_projects'
            AND column_name = 'priority'
        """)
        priority_exists = cur.fetchone()[0]

        if priority_exists == 0:
            print("❌ Priority column was not added to employee_projects table")
            return False

        print("✅ Table structures are correct")
        return True


def verify_indexes(conn) -> bool:
    """Verify that required indexes were created."""
    with conn.cursor() as cur:
        # Check for specific indexes
        cur.execute("""
            SELECT COUNT(*)
            FROM pg_indexes
            WHERE schemaname = 'employees'
            AND indexname IN ('idx_projects_status', 'idx_assignments_emp_proj', 'idx_milestones_due_date')
        """)
        index_count = cur.fetchone()[0]

        if index_count != 3:
            print(f"❌ Expected 3 required indexes, got {index_count}")
            return False

        print("✅ All required indexes are present")
        return True


def verify_project_data(conn) -> bool:
    """Verify that project data was inserted and updated correctly."""
    with conn.cursor() as cur:
        # Check project data after updates
        cur.execute("""
            SELECT project_name, start_date, end_date, budget, status, priority
            FROM employees.employee_projects
            ORDER BY project_name
        """)
        projects = cur.fetchall()

        if len(projects) != 3:
            print(f"❌ Expected 3 projects, found {len(projects)}")
            return False

        # Expected final state after all updates
        expected = {
            "Database Modernization": (
                "2024-01-15",
                "2024-06-30",
                287500.00,
                "active",
                "high",
            ),
            "Employee Portal Upgrade": (
                "2024-02-01",
                "2024-05-15",
                207000.00,
                "active",
                "medium",
            ),
            "HR Analytics Dashboard": (
                "2023-11-01",
                "2024-01-31",
                120000.00,
                "completed",
                "medium",
            ),
        }

        for project in projects:
            name = project[0]
            if name not in expected:
                print(f"❌ Unexpected project: {name}")
                return False

            exp = expected[name]
            # Use rows_match for comparison
            expected_row = (name,) + exp
            if not rows_match(project, expected_row):
                print(
                    f"❌ Project {name} data mismatch: expected {expected_row}, got {project}"
                )
                return False

        print("✅ Project data is correct")
        return True


def verify_assignment_data(conn) -> bool:
    """Verify that all current employees were assigned to projects by department."""
    with conn.cursor() as cur:
        # Check total assignment count matches current employee count
        cur.execute("""
            SELECT COUNT(*) FROM employees.project_assignments
        """)
        assignment_count = cur.fetchone()[0]

        cur.execute("""
            SELECT COUNT(DISTINCT de.employee_id)
            FROM employees.department_employee de
            WHERE de.to_date = '9999-01-01'
        """)
        current_employee_count = cur.fetchone()[0]

        if assignment_count != current_employee_count:
            print(
                f"❌ Expected {current_employee_count} assignments, found {assignment_count}"
            )
            return False

        # Check department-project mapping
        cur.execute("""
            SELECT d.dept_name, pa.project_id, pa.role, pa.allocation_percentage, COUNT(*)
            FROM employees.project_assignments pa
            JOIN employees.department_employee de ON pa.employee_id = de.employee_id AND de.to_date = '9999-01-01'
            JOIN employees.department d ON de.department_id = d.id
            JOIN employees.employee_projects ep ON pa.project_id = ep.project_id
            GROUP BY d.dept_name, pa.project_id, pa.role, pa.allocation_percentage
            ORDER BY d.dept_name
        """)
        dept_assignments = cur.fetchall()

        # Expected department-project mappings
        expected_mappings = {
            "Development": (1, "Developer", 80),
            "Human Resources": (2, "Business Analyst", 60),
            "Marketing": (3, "Marketing Specialist", 40),
            "Finance": (1, "Financial Analyst", 30),
            "Sales": (2, "Sales Representative", 50),
            "Research": (3, "Research Analyst", 70),
            "Production": (1, "Production Coordinator", 45),
            "Quality Management": (2, "QA Specialist", 85),
            "Customer Service": (3, "Customer Success", 35),
        }

        dept_found = {}
        for assignment in dept_assignments:
            dept_name, project_id, role, allocation, _ = assignment  # Ignore count
            if dept_name in dept_found:
                print(f"❌ Department {dept_name} has multiple assignments")
                return False
            dept_found[dept_name] = (project_id, role, allocation)

        for dept, expected in expected_mappings.items():
            if dept not in dept_found:
                print(f"❌ Department {dept} has no assignments")
                return False
            if dept_found[dept] != expected:
                print(
                    f"❌ Department {dept} assignment mismatch: expected {expected}, got {dept_found[dept]}"
                )
                return False

        # Check that all assignments have correct assigned_date
        cur.execute("""
            SELECT COUNT(*) FROM employees.project_assignments
            WHERE assigned_date != '2024-01-01'
        """)
        wrong_date_count = cur.fetchone()[0]

        if wrong_date_count > 0:
            print(f"❌ {wrong_date_count} assignments have incorrect assigned_date")
            return False

        print("✅ Assignment data is correct")
        return True


def verify_milestone_data(conn) -> bool:
    """Verify that milestone data was inserted and updated correctly."""
    with conn.cursor() as cur:
        cur.execute("""
            SELECT project_id, milestone_name, due_date, completed
            FROM employees.project_milestones
            ORDER BY project_id, milestone_name
        """)
        milestones = cur.fetchall()

        if len(milestones) != 6:
            print(f"❌ Expected 6 milestones, found {len(milestones)}")
            return False

        # Expected milestones
        expected_milestones = {
            (1, "Design Phase Complete"): ("2024-03-01", False),
            (1, "Implementation Complete"): ("2024-05-15", False),
            (2, "UI/UX Approval"): ("2024-03-15", False),
            (2, "Beta Testing"): ("2024-04-30", False),
            (3, "Data Collection"): ("2023-12-15", True),  # Should be completed
            (3, "Dashboard Launch"): ("2024-01-25", False),
        }

        for milestone in milestones:
            project_id, name, due_date, completed = milestone
            key = (project_id, name)

            if key not in expected_milestones:
                print(f"❌ Unexpected milestone: {key}")
                return False

            expected_due, expected_completed = expected_milestones[key]
            if str(due_date) != expected_due or completed != expected_completed:
                print(
                    f"❌ Milestone {name} mismatch: expected ({expected_due}, {expected_completed}), got ({due_date}, {completed})"
                )
                return False

        print("✅ Milestone data is correct")
        return True


def verify_single_department_membership(conn) -> bool:
    """Verify that each current employee belongs to only one active department."""
    with conn.cursor() as cur:
        # 查找当前在职且关联多个部门的员工
        cur.execute("""
            SELECT de.employee_id, COUNT(*) AS dept_count
            FROM employees.department_employee de
            WHERE de.to_date = '9999-01-01'
            GROUP BY de.employee_id
            HAVING COUNT(*) > 1
        """)
        multi_dept_employees = cur.fetchall()

        if len(multi_dept_employees) > 0:
            print("❌ 存在当前属于多个部门的员工：")
            for employee_id, dept_count in multi_dept_employees:
                print(f" - 员工 {employee_id} 属于 {dept_count} 个部门")
            return False

        print("✅ 所有当前员工均仅属于一个部门")
        return True


def verify_employee_count_consistency(conn) -> bool:
    """Verify that sum of current employees by department equals total current employee count."""
    with conn.cursor() as cur:
        # 统计当前员工总数
        cur.execute("""
            SELECT COUNT(DISTINCT de.employee_id)
            FROM employees.department_employee de
            WHERE de.to_date = '9999-01-01'
        """)
        total_employee_count = cur.fetchone()[0]

        # 按部门汇总当前员工数
        cur.execute("""
            SELECT d.dept_name, COUNT(DISTINCT de.employee_id) AS emp_count
            FROM employees.department_employee de
            JOIN employees.department d ON d.id = de.department_id
            WHERE de.to_date = '9999-01-01'
            GROUP BY d.dept_name
            ORDER BY d.dept_name
        """)
        dept_counts = cur.fetchall()

        print("部门员工人数明细：")
        dept_sum = 0
        for dept_name, emp_count in dept_counts:
            print(f" - {dept_name}: {emp_count}")
            dept_sum += emp_count

        print(f"\n部门汇总员工数: {dept_sum}")
        print(f"直接统计员工数: {total_employee_count}")

        # 一致性判断
        if dept_sum != total_employee_count:
            print(
                f"❌ 通用统计不一致：部门求和({dept_sum}) 不等于总人数({total_employee_count})"
            )
            return False

        print("✅ 部门汇总与总员工数量一致")
        return True


def main():
    """Main verification function."""
    print("=" * 50)

    # Get connection parameters
    conn_params = get_connection_params()

    if not conn_params["database"]:
        print("❌ No database specified")
        sys.exit(1)

    try:
        # Connect to database
        conn = psycopg2.connect(**conn_params)

        # Verify all components
        success = (
            verify_table_structures(conn)
            and verify_indexes(conn)
            and verify_project_data(conn)
            and verify_assignment_data(conn)
            and verify_milestone_data(conn)
        )

        conn.close()

        if success:
            print("\n🎉 Task verification: PASS")
            sys.exit(0)
        else:
            print("\n❌ Task verification: FAIL")
            sys.exit(1)

    except psycopg2.Error as e:
        print(f"❌ Database error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Verification error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
