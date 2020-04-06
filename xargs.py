# Collection of arguments
def multipy(*numbers):
    # print(numbers) # Returns tuple.

    total = 1

    for number in numbers:
        total *= number
    
    return total

result = multipy(2, 3, 4, 5)

print(f"Result for collection args: {result}")