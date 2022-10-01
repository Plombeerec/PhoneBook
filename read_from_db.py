import json

with open('phonebook.json', encoding='utf-8') as f:
    capitals_json = f.read()

capitals = json.loads(capitals_json)
print(capitals)

