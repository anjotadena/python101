# [] - Lists
# A sequence of objects

letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 3]]
zeros = [0] * 10

combined = zeros + letters

numbers = list(range(20))

chars = list("Hello, World")

print(zeros)
print(combined)
print(numbers)
print(chars) # len(chars) - get length of list


# Accessing list items
print(letters[-1]) # Last item
print(letters[0:3]) # Slice
print(letters[:]) # copy of original list
print(numbers[::2]) # Steps 
print(numbers[::-1]) # Reverse a list


numbers = [1, 2, 3]
first = numbers[0]
second = numbers[1]
third = numbers[3]

# Unpacking lists
first, second, third = numbers # Must be equal size
first, *other_number = numbers # Packing all other in separate list
first, *other, last = numbers # Unpacking first and last item
