# String methods
# String is an object and we can access methods or functions inside object
cource = "Python with love"

print(f"Upper Case function: {cource.upper()}")
print(f"Lover Case function: {cource.lower()}")
print(f"Title string function: {cource.title()}")
print(f"Title string function: {cource.strip()}") # Remove whitespace from beginning and end string
print(f"Find love: {cource.find('love')}") # Return chracter index
print(f"Replace love with WHAT?: {cource.replace('love', 'WHAT?')}")
print(f"Inword: {'love' in cource}")
print(f"Doesn't exist word: {'hate' not in cource}")
