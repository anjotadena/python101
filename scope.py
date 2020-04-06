# Stays on memory for a longer time
message = "a" # Global variable

def greet(message): # Function scope variable
    message = 'aa'

    print(message)