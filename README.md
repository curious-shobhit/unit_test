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

## Folder Structure



Execution Steps
Draft test cases within the tests/test_employee_department_queries.py file.
Invoke the test execution using pytest along with the command pytest --docker-compose=docker-compose.yml.

