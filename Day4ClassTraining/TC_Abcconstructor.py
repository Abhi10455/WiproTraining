from abc import ABC, abstractmethod
class employee:
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def salary(self):
        pass
class Manager(employee):
    def salary(self):
        print(self.name,"salary is 600000")

m=Manager("abhi")
m.salary()