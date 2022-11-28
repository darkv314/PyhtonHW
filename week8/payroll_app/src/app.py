from employee import SalesAssociate, AdmistrativeWorker, ManufacturingWorker
import payroll as hr

def main():
    salary_employee = AdmistrativeWorker(1, 'John Doe', 1500)
    hourly_employee = ManufacturingWorker(2, 'Jane Doe', 40, 15)
    commission_employee = SalesAssociate(3, 'Foo Fighter', 1000, 250)
    payroll_system = hr.PayrollSystem()
    payroll_system.calculate_payroll([
        salary_employee,
        hourly_employee,
        commission_employee
    ])


if __name__ == "__main__":
    main()
