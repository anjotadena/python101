# Loop to create a repetion

# range start with 0 by default
# range(start, end, steps)
for number in range(1, 6): # Repeated 5 times
    # print(f"Number: {number + 1}")
    print("Attempt", number, number * ".")


# FOR ELSE LOOP
successful = False

for number in range(5):
    print("Attempt")

    if successful:
        print("Success...")
        break # Exit automatically in loop
else:
    print("Attempted 5 times and failed")

# NESTED LOOP
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")
