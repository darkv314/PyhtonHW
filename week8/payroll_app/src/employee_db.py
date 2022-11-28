from employee import Employee, AdmistrativeWorker, SalesAssociate, ManufacturingWorker
import copy

class EmployeeDatabase:
    def __init__(self):
        self.__employees = [
            {
                'id': 1,
                'name': 'John Doe',
                'role': 'manager', # is a Admistrative Worker
                'weekly_salary': 1500
            },
            {
                'id': 2,
                'name': 'Jane Doe',
                'role': 'factory', # is a Manufacturing Worker
                'worked_hours': 40,
                'hour_rate': 15
            },
            {
                'id': 3,
                'name': 'Foo Fighter',
                'role': 'sales', # is a Sales Associate
                'fixed_salary': 1000,
                'comission': 250
            }
        ]


    def get_employees(self):
        """Returns a list of objects whose parent is class Employee"""
        return [self.__create_employee(copy.deepcopy(employee)) for employee in self.__employees]


    def __create_employee(self, raw_data):
        role = raw_data.pop('role')
        match role:
            case 'manager':
                return AdmistrativeWorker(*raw_data.values())
            case 'factory':
                return ManufacturingWorker(*raw_data.values())
            case 'sales':
                return SalesAssociate(*raw_data.values())
