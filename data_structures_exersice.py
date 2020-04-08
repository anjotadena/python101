from pprint import pprint

# FIND THE MOST REPEATED CHARACTER
sentence = "This is a common interview question"

characters = dict()
max_key = dict()
for c in sentence:
    if c not in characters:
        characters[c] = 0
    characters[c] += 1
    
    # max_key[c] = characters[c]

    # if (max_key[c])

# print(characters)
pprint(characters)
max_key = None

for k in characters:
    if max_key == None:
        max_key = dict(key=k, value=characters[k])
    
    if characters[k] > max_key.get('value'):
        max_key = dict(key=k, value=characters[k])

pprint(max_key)
