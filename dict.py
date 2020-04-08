# Collection of key value per
# key -> value
# Value could be any type
point = { "x": 1, "y": 5 }

# dict()

point = dict(x=1, y=2) # set Key arguments

# Access dict item
print(point["x"])
print(point.get("y"))

# Add key
point["z"] = 3
print(point["z"])

if "a" in point:
    print(point["a"])

# Set default if empty key
print(point.get("a", 0))

# Delete key value
del point["z"]

print(point)

for key in point:
    print(key, point[key])

for key, value in point.items():
    print(key, value)


# Dict comprehensions
values = []

for x in range(5):
    values.append(x * 2)
print(values)

values = [x * 2 for x in range(5)]
print(values)

values = {x * 2 for x in range(5)}
print(values)
