from src.employee import ManufacturingWorker

def test_admin_instance():
    manufacturing_checker = {
        'id': 1,
        'name': 'Hernan',
        'hours_worked': 12,
        'hour_rate': 16
    }
    new_admin = ManufacturingWorker(1, 'Hernan', 12, 16)
    assert type(new_admin) is ManufacturingWorker
    # assert type(new_admin) is AdmistrativeWorker
    assert new_admin.id == manufacturing_checker['id']
    assert new_admin.name == manufacturing_checker['name']
    assert new_admin.hours_worked == manufacturing_checker['hours_worked']
    assert new_admin.hour_rate == manufacturing_checker['hour_rate']

def test_admin_calculate_payroll():
    new_admin = ManufacturingWorker(1, 'Hernan', 12, 16)
    assert new_admin.calculate_payroll() == 192
