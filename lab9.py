from abc import ABC, abstractmethod
from typing import List

# Інтерфейс Відвідувача
class Visitor(ABC):
    @abstractmethod
    def visit_company(self, company) -> None:
        pass

    @abstractmethod
    def visit_department(self, department) -> None:
        pass

    @abstractmethod
    def visit_employee(self, employee) -> None:
        pass

# Інтерфейси для відвідуваних класів
class Element(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass

# Клас Компанії
class Company(Element):
    def __init__(self, departments: List['Department']):
        self.departments = departments

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_company(self)

# Клас Департаменту
class Department(Element):
    def __init__(self, employees: List['Employee']):
        self.employees = employees

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_department(self)

# Клас Співробітника
class Employee(Element):
    def __init__(self, position: str, salary: float):
        self.position = position
        self.salary = salary

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_employee(self)

# Конкретний Відвідувач для формування "Зарплатної відомості"
class SalaryReportVisitor(Visitor):
    def visit_company(self, company: Company) -> None:
        print("Зарплатна відомість для компанії:")
        for department in company.departments:
            department.accept(self)

    def visit_department(self, department: Department) -> None:
        print("Зарплатна відомість для департаменту:")
        for employee in department.employees:
            employee.accept(self)

    def visit_employee(self, employee: Employee) -> None:
        print(f"Посада: {employee.position}, Зарплата: {employee.salary}")

if __name__ == "__main__":
    employee1 = Employee("Інженер", 1000)

    employee2 = Employee("Менеджер", 1200)
    employee3 = Employee("Бухгалтер", 1100)

    department1 = Department([employee1, employee2])
    department2 = Department([employee3])

    company = Company([department1, department2])

    salary_report_visitor = SalaryReportVisitor()

    company.accept(salary_report_visitor)

    department1.accept(salary_report_visitor)
