import pytest

def test_employee_details_query(redshift_connection):
    # Sample test case implementation
    cursor = redshift_connection.cursor()
    cursor.execute('SELECT id, name FROM employees;')
    result = cursor.fetchall()
    assert len(result) == 2

def test_employee_count_by_department(redshift_connection):
    # Sample test case implementation
    cursor = redshift_connection.cursor()
    cursor.execute('SELECT department_id, COUNT(*) FROM employees GROUP BY department_id;')
    result = cursor.fetchall()
    assert len(result) == 2
