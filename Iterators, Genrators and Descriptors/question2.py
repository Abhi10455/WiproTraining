class SalaryDescriptor:
    def __get__(self, obj, objtype=None):
        return obj._salary
    def __set__(self, obj, value):
        if value <= 0:
            raise ValueError("Salary must be a positive number")
        obj._salary = value

class Employee:
    salary = SalaryDescriptor()

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
emp1 = Employee("Abhi", 50000)
emp2 = Employee("Ravi", 65000)

print(emp1.name, emp1.salary)
print(emp2.name, emp2.salary)
try:
    emp3 = Employee("Neha", -30000)
except ValueError as e:
    print("Error:", e)


