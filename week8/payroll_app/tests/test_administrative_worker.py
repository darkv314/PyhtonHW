from src.employee import AdmistrativeWorker

def test_admin_instance():
    admin_checker = {
        'id': 1,
        'name': 'Hernan',
        'weekly_salary': 100
    }
    new_admin = AdmistrativeWorker(1, 'Hernan', 100)
    assert type(new_admin) is AdmistrativeWorker
    assert new_admin.id == admin_checker['id']
    assert new_admin.name == admin_checker['name']
    assert new_admin.weekly_salary == admin_checker['weekly_salary']

def test_admin_calculate_payroll():
    new_admin = AdmistrativeWorker(1, 'Hernan', 100)
    assert new_admin.calculate_payroll() == 100
