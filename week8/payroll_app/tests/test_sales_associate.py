from src.employee import SalesAssociate, AdmistrativeWorker

def test_admin_instance():
    sales_checker = {
        'id': 1,
        'name': 'Hernan',
        'weekly_salary': 100,
        'commission': 12
    }
    new_admin = SalesAssociate(1, 'Hernan', 100, 12)
    assert type(new_admin) is SalesAssociate
    # assert type(new_admin) is AdmistrativeWorker
    assert new_admin.id == sales_checker['id']
    assert new_admin.name == sales_checker['name']
    assert new_admin.weekly_salary == sales_checker['weekly_salary']
    assert new_admin.commission == sales_checker['commission']

def test_admin_calculate_payroll():
    new_admin = SalesAssociate(1, 'Hernan', 100, 12)
    assert new_admin.calculate_payroll() == 112
