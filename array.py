from array import array

numbers = array("i", [1, 2, 3])

# numbers[0] = 'sad' # Errror
numbers.insert(4, 1)
numbers.remove(1)
numbers[0] = 6

print(numbers)