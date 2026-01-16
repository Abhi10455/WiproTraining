from abc import ABC,abstractmethod
class bank(ABC):
    @abstractmethod
    def interest(self):
        pass
    @abstractmethod
    def loan(self):
        pass

class SBI(bank):
    def interest(self):
        print("interest is 6%")
    def loan(self):
        print("loan is available")

s=SBI()
s.interest()
s.loan()