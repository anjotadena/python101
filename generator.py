from sys import getsizeof
# Generator comprehensions

values = (x * 2 for x in range(100000))

print("Generator size: ", getsizeof(values))

values = [x * 2 for x in range(1000000)]
print("list size: ", len(values))