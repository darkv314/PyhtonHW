from src.employee import Employee

class PayrollSystem:

    def calculate_payroll(self, employees):
        if employees is not None:
            for employee in employees:
                if issubclass(type(employee), Employee):
                    print(f'Payroll for: {employee}')
                    print(f'Check amount: {employee.calculate_payroll()}')

        else:
            return None