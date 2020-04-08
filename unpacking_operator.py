numbers = [1, 2, 3]

print(*numbers)

first = [1, 2, 3]
second = [4, 5, 6]

print([*first, *second])

first = dict(x=1)
second = dict(x=1, y=2, z=3)
combined = {**first, **second}

print(combined)
