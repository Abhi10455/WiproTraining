class Vehicle:
    vehicle_count = 0
    def __init__(self):
        Vehicle.vehicle_count += 1

    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)

    def drive(self):
        print("Car is driving")

class ElectricCar(Car):
    def __init__(self):
        Car.__init__(self)

    def charge(self):
        print("Electric car is charging")

v1 = Vehicle()
c1 = Car()
e1 = ElectricCar()

v1.start()
c1.start()
c1.drive()
e1.start()
e1.drive()
e1.charge()

print("\nTotal vehicles created:", Vehicle.vehicle_count)
