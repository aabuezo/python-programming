file = open('csv_data.csv', 'r')
lines = file.readlines()
file.close()

lines = [line.strip() for line in lines[1:]]   # quitar la linea de encabezado
for line in lines:
    person_data = line.split(',')
    name = person_data[0].title()
    age = person_data[1]
    univ = person_data[2].title()
    degree = person_data[3].title()

    print(f'{name} is {age} studying {degree} at {univ}')


# for writing
csv_values = ','.join(['Rolf', '25', 'MIT', 'Computer Science'])
print(csv_values)
