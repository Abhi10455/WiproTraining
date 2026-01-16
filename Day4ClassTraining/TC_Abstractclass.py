from abc import ABC, abstractmethod
class shape(ABC):
    def display(self):
        print("normal method")
    @abstractmethod
    def area(self):
        pass

class Rectangle(shape):
    def area(self):
        print("area method implemented")

r=Rectangle()
r.area()
r.display()