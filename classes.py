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
