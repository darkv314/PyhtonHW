import payroll as hr
from employee_db import EmployeeDatabase

def main():
    employees = EmployeeDatabase().get_employees()
    payroll_system = hr.PayrollSystem()
    payroll_system.calculate_payroll(employees)


if __name__ == "__main__":
    main()
