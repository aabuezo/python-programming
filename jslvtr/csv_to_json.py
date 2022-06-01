# read csv file
import json

with open('csv_file.txt', 'r') as file:
    lines = file.readlines()

# convert lines to a list of dicts
data = []
for line in lines:
    club, city, country = line.strip().split(',')
    obj = {'club': club, 'city': city, 'country': country}
    data.append(obj)

# write data to json_file.txt
with open('json_file.txt', 'w') as file:
    json.dump(data, file)
