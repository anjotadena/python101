class Animal:
    def eat(self):
        print("Eating...")

# Animal: Base, Parent
# Mammal: Child, Sub

class Mammal(Animal): # Inherit all Animal attributes/methods
    def walk(self):
        print("Walking...")

class Fish(Animal):
    def swim(self):
        print("Swimming...")

m = Mammal()

m.eat()

