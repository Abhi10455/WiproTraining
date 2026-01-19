class Calculator:
    def calculate(self, a, b):
        print("Cal: Adding numbers")
        return a + b

class AdvancedCalculator(Calculator):
    def calculate(self, a, b):
        print("AdvCal: Multiplying numbers")
        return a * b

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

calc = Calculator()
adv_calc = AdvancedCalculator()

print(calc.calculate(5, 3))
print(adv_calc.calculate(5, 3))
n1 = Number(10)
n2 = Number(20)
result = n1 + n2

print("Result of adding objects:", result.value)
