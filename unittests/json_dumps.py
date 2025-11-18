import json

python_data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

names = ['William', 'Samson', 'Emmanuel', 'Isaac']

json_string = json.dumps(names, indent=4) # indent for pretty printing
print(json_string)