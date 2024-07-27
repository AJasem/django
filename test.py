import codecs

# Read the file with the correct encoding
with codecs.open('data.json', 'r', 'utf-8-sig') as f:
    data = f.read()

# Write it back without BOM
with open('data.json', 'w', encoding='utf-8') as f:
    f.write(data)