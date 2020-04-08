# Collection of no duplicates
numbers = [1, 1, 2, 3, 4, 4, 3]
print(numbers)
# Remove duplicatate
# Convert it to set
uniques = set(numbers)
print(uniques)


uniques.add(5)
print(uniques)
uniques.remove(5)
print(uniques)
first = set(numbers)
second = {1, 4}

print(first | second)

# Get intersection
print(first & second)

# Get diff
print(first - second)

# Symmetric diff
print(first ^ second)

# Access set
if 1 in first:
    print("yes")
