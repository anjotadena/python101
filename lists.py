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
third = numbers[2]

# Unpacking lists
first, second, third = numbers # Must be equal size
first, *other_number = numbers # Packing all other in separate list
first, *other, last = numbers # Unpacking first and last item

# Looping over list

for index, letter in enumerate(letters):
    # print(letters) (index, value)
    print(index, letter)

todos = []

# Add item
todos.append('Study python')
print(todos)

# Add item to the specific index
todos.insert(0, 'Study PHP')
print(todos)

# Remove item
todos.pop(0) # remove 1 item by index
print(todos)

todos.remove('Study python') # First occurring will be removed

print(todos)

# Removed items starting from index 0
# del todos[0:2] 

# remove all items
todos.clear()


# Finding item

letters = ["a", "b", "c"]

if "d" in letters:
    print(letters.index("d"))



numbers = [3, 51, 2, 8, 6]

# numbers.sort(reverse=True)

print(sorted(numbers, reverse=True))

print(numbers)

items = [
    ("Product1", 10),
    ("Product2", 3),
    ("Product3", 1),
    ("Product4", 6),
]

def sort_item(item):
    return item[1]

items.sort(key=sort_item)

print(items)
