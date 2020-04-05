# String is a sequence of characters

name = "Anjo"

message = """
Hi, Anjo

Blah blah blah...
"""

print(name)
print(message)

# Number of characters of name variable
print(len(name))

# Access character
print(name[0]) # First character
print(name[-1]) # Last character

# access starting from first character until length of 3
print(name[0:3])

# access character startinf from first character to the end
print(name[0:])

# Access first character with length of 3
print(name[:3])

# Copy of original strings
print(name[:])
