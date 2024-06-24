name = []
for text in 'Human':
    name.append(text)
print(name)
# Output is: ['H', 'u', 'm', 'a', 'n']

name = [text for text in 'Human']
print(name)
# Output is: ['H', 'u', 'm', 'a', 'n']

print([text for text in 'Human'])
# Output is: ['H', 'u', 'm', 'a', 'n']