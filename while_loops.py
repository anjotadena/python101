# number = 10

# while number > 0:
#     print(number)

#     number //= 2 # Ogmented assignment operator

# command = ""

# while command.lower() != "quit":
#     command = input("> ")

#     print("ECHO:", command)

for number in range(1, 11):
    if number % 2:
        print("Odd:", number)
    else:
        print("Even:", number)
