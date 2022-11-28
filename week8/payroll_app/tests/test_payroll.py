from src.payroll import PayrollSystem
from src.employee import AdmistrativeWorker, ManufacturingWorker, SalesAssociate

def test_instance():
    new_payroll = PayrollSystem()
    assert type(new_payroll) is PayrollSystem

def test_calculate_payroll():
    employee1 = AdmistrativeWorker(1, 'Pedro', 1200)
    employee2 = ManufacturingWorker(2, 'Juan', 40, 12)
    employee3 = SalesAssociate(3, 'Maria', 1000, 12)
    new_payroll = PayrollSystem()
    new_payroll.calculate_payroll([employee1, employee2, employee3])

def test_calculate_payroll_empty_list():
    new_payroll = PayrollSystem()
    new_payroll.calculate_payroll([])


def test_calculate_payroll_none_list():
    new_payroll = PayrollSystem()
    new_payroll.calculate_payroll([None, None, None])


def test_calculate_payroll_none():
    new_payroll = PayrollSystem()
    new_payroll.calculate_payroll(None)