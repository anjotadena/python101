# A read only list
# Immutable
# cannot add, remove, modify, udpate item

# point = (1, 2)
point = 1, 2
point = 1,
point = () # Empty tuple

point = (1, 2) + (3, 4)
point = (1, 2) * 10

print(type(point))
print(point)
print(point[0:2])

point = (5, 10)
# Unpack tuple
x, y = point