temperature = 39

# As long as indented there belong to if block
if temperature > 38:
    print("Positive for COVID-19.")
elif temperature > 33:
    print("You're good.")
else:
    print('Naah...')
# print("Please take a rest.")

# Ternary operator
age = 22
is_eligible = "Yes" if age >= 18 else "No"

print(f"Your eligible fo scholar: {is_eligible}")