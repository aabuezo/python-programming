# open for reading
my_file = open('data.txt', 'r')
my_file_content = my_file.read()
my_file.close()

print(my_file_content)

# open for writing
user_name = input('Enter your name: ')
my_file_writing = open('data.txt', 'w')     # 'w' overwrites!!
my_file_writing.write(user_name)
my_file_writing.close()

# copying a file
input_file = open('people.txt', 'r')
names = [line.strip() for line in input_file.readlines()]   # 'Rolf\n' - quita el \n
# print(type(names))
input_file.close()

output_file = open('people_copy.txt', 'w')
for name in names:
    output_file.write(f'{name}\n')      # vuelvo a meter el \n
output_file.close()

