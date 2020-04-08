# Stack operations
# LIFO = Last In First Out
items = []

# Add item
items.append(1)
items.append(2)
items.append(3)
items.append(4)
items.append(5)

# Remove last item
last = items.pop()

print(last)

# Get last item
print(items[-1])

# Falsy values
# ""
# []
# 0

if not items:
    print("No items.")
