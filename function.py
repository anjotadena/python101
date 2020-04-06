def greet(first_name, last_name):
    print(f"Hi there {first_name} {last_name}")
    print("Welcome aboard")

greet("Anjo", "Tadena")

# 1 - Perform a task
# 2 - Return a value

# round(1.9)

def get_greeting(name):
    return f"Hi {name}"


print(get_greeting("Anjo"))

def increment(number, by):
    return number + by

# result = increment(2, 1)
result = increment(2, by=1)

print(f"Increment result: {result}")

def decrement(number, by=1): # Optional parameter
    return number - by

print(f"Decrement result with default parameter value: {decrement(2)}")
