# A class is a blueprint for creating a new objects
# Object: Instance of a class

# Class: Human
# Objects: John, Marie, Jean

class Point:
    # Class level atrributes
    default_color = "red" # shared all instances of a class

    # Self is a reference of current object
    # Constructor:
    def __init__(self, x, y):
        # Instance attributes     
        self.x = x
        self.y = y

        self.__p = 10 # Private attribute

    # Methods - a function inside a class
    def draw(self):
        print(f"Point coordinate: x: {self.x}, y: {self.y}")

    # Class level methods
    @classmethod # Decorator
    def zero(cls): # Reference to a class
        return cls(0, 0)

point = Point(5, 20)

print(type(point))

print(isinstance(point, Point))

# print(f"Point coordinate: x: {point.x}, y: {point.y}")
point.draw()
print(f"Default color: {point.default_color}")
Point.default_color = "YELLOW"
print(f"Default color: {point.default_color}")

point = Point.zero()
point.draw()


class Product:
    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Value cannot be negative.")
        self.__price = value

product = Product(10)

print(product.price)

product.price = 100
print(product.price)

# Throw value error exception
product.price = -10
