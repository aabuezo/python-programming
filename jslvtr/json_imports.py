import json

# reading from file
file = open('friends.json', 'r')
file_contents = json.load(file)     # reads file and turns it into dictionary
file.close()

print(file_contents['friends'][0])

# writing to a file
cars = [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Ford', 'model': 'Focus'}
]

file = open('cars.json', 'w')
json.dump(cars, file)
file.close()

# json with strings
my_json_string = '[{"name": "Alfa Romeo", "released": 1950}]'
incorrect_car = json.loads(my_json_string)
print(incorrect_car[0]['name'])
