class Mammal:
    def mammal_info(self):
        print("Mammals can give direct birth.")

class WingedAnimal:
    def winged_animal_info(self):
        print("Winged animals can flap.")

class Bat(Mammal, WingedAnimal):
    pass

my_bat = Bat()
my_bat.mammal_info()
my_bat.winged_animal_info()


print(type(my_bat))

# checking the base classes of a class object
print(type(my_bat).__bases__)

# method resolution order
print(type(my_bat).__mro__)
