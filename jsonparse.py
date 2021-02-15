import json

# a Python object (dict):
x = {
   "name": "John",
   "age": 30,
   "city": "New York",
   "wind": {"speed": 6.15, "deg": 141}
}

# convert into JSON:
y = json.dumps(x)
print(x['name'])
print(x['age'])
print(x['wind'])
print(x['wind']['speed'])
print(x['wind']['deg'])

# the result is a JSON string:
print(y)

