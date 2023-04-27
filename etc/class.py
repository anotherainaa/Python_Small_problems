class Animal:
    name = ""

    def eat(self):
        print("I can eat")


class Dog(Animal):
    def __init__(self, name, age):
        """ Initalize name and age attributes """
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting.")


max = Dog('Max', 3)

print(f"My dog's name is {max.name}.")
max.sit()

max.eat()

print(type(max))

# checking the base classes of a class object
print(max.__class__.__bases__)
