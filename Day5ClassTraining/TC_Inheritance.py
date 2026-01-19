class Animal:
    def speak(self):
        print("Animal makes a sound")

class dog(Animal):
    def bark(self):
        print("Dog makes a bark")

d=dog()
d.speak()
d.bark()
