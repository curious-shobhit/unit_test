# Vision Document: Automated Redshift Unit Testing with Dockerized Environment

## Project Overview

The project aims to establish an automated unit testing framework for Amazon Redshift SQL queries, leveraging a Dockerized environment. The framework will empower data engineers and analysts to develop and execute consistent unit tests for Redshift SQL queries within an isolated ecosystem.

## Objectives

- Create a modular and adaptable framework for composing and executing unit tests tailored for Redshift SQL queries.
- Utilize Docker Compose to construct a Dockerized environment encompassing a simulated Redshift database.
- Offer a convenient approach for specifying test data, tables, views, indexes, and user grants through SQL scripts and CSV files.
- Automate the configuration of the test environment, the loading of test data, and the execution of tests.
- Seamlessly integrate with `pytest` to facilitate the execution of tests and the production of comprehensive test reports.

## Features

1. **Folder Structure and Test Data Setup:**

   - Organize the project with a structured hierarchy to manage SQL scripts, test data, and test scripts.
   - Place SQL scripts for generating tables, views, indexes, and user grants in the `sql_scripts` directory.
   - Employ the `test_data` directory for storing CSV files representing test data.

2. **Dockerized Environment:**

   - Utilize Docker Compose to define a Dockerized environment housing a simulated Redshift database.
   - Incorporate environment variables within the `docker-compose.yml` file to configure database connection parameters.

3. **Test Execution:**

   - Develop `redshift_simulator.py` to establish the test environment, generate tables, load test data, and execute SQL scripts.
   - Employ `psycopg2` for connecting to the Redshift database and executing SQL statements.
   - Traverse the `sql_scripts` directory to execute SQL scripts for table creation, views, indexes, and grants.
   - Utilize the `COPY` command to load data from CSV files into corresponding tables.

4. **Test Definition and Execution:**

   - Compose test cases as Python scripts utilizing the `pytest` framework.
   - Leverage the `pytest-docker-compose` plugin to manage the Dockerized environment during test execution.
   - Define test scenarios that establish connections to the Dockerized Redshift database and execute SQL queries.
   - Generate detailed test reports and output using `pytest` capabilities.

#### Example Test Scenarios and Coverage

Our comprehensive test scenarios cover key aspects of our Employee Department database, including:

1.  Employee and Department Details Query

    -   Test Case 1: Verify the accuracy of retrieving employee and department details.
    -   Test Case 2: Validate the presence of specific employees in particular departments.
2.  Employee Count by Department Query

    -   Test Case 3: Confirm the accuracy of employee counts in each department.

#### Test Environment Setup

We will establish a dedicated Dockerized Redshift simulation environment that closely mimics our production setup. The following components are integral to the setup:

##### Folder Structure:

Copy code

![image](https://github.com/curious-shobhit/unit_test/assets/57742116/0ea0ab43-83d0-4f81-8a74-54506d228b47)


1.  Dockerfile (`docker/Dockerfile`): A Dockerfile to configure the Redshift simulation environment:

    DockerfileCopy code

    `FROM awslabs/amazon-redshift-utils

    # Copy test data and SQL scripts to the container
    COPY test_data /test_data
    COPY sql_scripts /sql_scripts

    # Set environment variables
    ENV DB employeedb
    ENV HOST localhost
    ENV PORT 5439
    ENV USER testuser
    ENV PASSWORD testpassword

    # Run Redshift simulation
    CMD ["python3", "redshift_simulator.py"]`

2.  SQL Scripts (`sql_scripts/`): Directory containing SQL script files (`script1.sql`, `script2.sql`, etc.) with your Redshift queries.

3.  Test Scripts (`tests/`):

    -   `conftest.py`: Configuration file for `pytest`, defining fixtures and shared resources.

    pythonCopy code

    `# conftest.py
    import pytest
    import psycopg2
    import os

    @pytest.fixture(scope="module")
    def redshift_connection():
        conn = psycopg2.connect(
            dbname=os.environ["DB"],
            user=os.environ["USER"],
            password=os.environ["PASSWORD"],
            host=os.environ["HOST"],
            port=os.environ["PORT"]
        )
        yield conn
        conn.close()`

    -   `test_employee_department_queries.py`: Test script containing unit test cases.

    pythonCopy code

    `# test_employee_department_queries.py
    import pytest

    def test_employee_details_query(redshift_connection):
        # ... (test case implementation)

    def test_employee_count_by_department(redshift_connection):
        # ... (test case implementation)`

4.  `pytest.ini`: Configuration file for `pytest` specifying command-line options and test discovery settings.

    cssCopy code

    `[pytest]
    addopts = --docker-compose=docker-compose.yml`

5.  `redshift_simulator.py`: Python script to load data from CSV files and execute SQL scripts against the Redshift simulation.

    pythonCopy code

    `# redshift_simulator.py
    import psycopg2
    from psycopg2 import sql
    import os

    def main():
        conn = psycopg2.connect(
            dbname=os.environ["DB"],
            user=os.environ["USER"],
            password=os.environ["PASSWORD"],
            host=os.environ["HOST"],
            port=os.environ["PORT"]
        )

        data_dirs = [
            os.path.join(os.path.dirname(__file__), "test_data"),
            os.path.join(os.path.dirname(__file__), "sql_scripts")
        ]

        try:
            with conn.cursor() as cursor:
                for data_dir in data_dirs:
                    for root, dirs, files in os.walk(data_dir):
                        for file in files:
                            if file.endswith(".csv"):
                                table_name = os.path.splitext(file)[0]
                                csv_file = os.path.join(root, file)
                                with open(csv_file, "r") as file:
                                    cursor.copy_expert(f"COPY {table_name} FROM stdin CSV HEADER", file)
                            elif file.endswith(".sql"):
                                sql_file = os.path.join(root, file)
                                with open(sql_file, "r") as file:
                                    sql_statements = file.read()
                                    cursor.execute(sql.SQL(sql_statements))
            conn.commit()
        except Exception as e:
            print("Error:", e)
        finally:
            conn.close()

    if __name__ == "__main__":
        main()`

### Test Execution Steps

#### Test Employee Department Queries (`test_employee_department_queries.py`):

pythonCopy code

`# test_employee_department_queries.py
import pytest

def test_employee_details_query(redshift_connection):
    # ... (test case implementation)

def test_employee_count_by_department(redshift_connection):
    # ... (test case implementation)`

### Continuous Integration and Continuous Deployment (CI/CD) Integration

Our CI/CD pipeline will automatically trigger unit tests upon each code commit, ensuring thorough validation before integration.

### Reporting and Documentation

Detailed test reports will provide
