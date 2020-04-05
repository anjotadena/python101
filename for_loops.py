# Loop to create a repetion

# range start with 0 by default
# range(start, end, steps)
for number in range(1, 6): # Repeated 5 times
    # print(f"Number: {number + 1}")
    print("Attempt", number, number * ".")


successful = False

for number in range(5):
    print("Attempt")

    if successful:
        print("Success...")
        break # Exit automatically in loop
else:
    print("Attempted 5 times and failed")
