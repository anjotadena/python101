# Stays on memory for a longer time
message = "a" # Global variable
global_var = 'h'

def greet(message): # Function scope variable
    global global_var # Access global message variable
    
    message = 'aa'

    print(message)