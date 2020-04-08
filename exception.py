# Exception where error terminates the program

try:
    age = int(input("Age: "))
except ValueError as ex:
    print(ex)
else:
    print("No exceptions were thrown.")