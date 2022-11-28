import pytest
from src.employee import Employee, AdmistrativeWorker

def test_employee_no_instance():
    with pytest.raises(expected_exception=TypeError):
        Employee(1, 'Hernan')


