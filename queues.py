from collections import deque

# QUEUES
#  FIFO - First In Last Out

items = deque([])

items.append(1)
items.append(2)
items.append(3)
items.append(4)
items.append(5)

items.popleft()

if not items:
    print("No items.")
