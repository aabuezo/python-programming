cars = ['ok', 'ok', 'ok', 'faulty', 'ok', 'ok']

for car in cars:
    print(f'Status: {car}')
    if car == 'faulty':
        print('Stopping the production line!')
        break
    print('Sending car to customer.')
else:   # solo si no hubo break ni error en el for loop!!
    print('All cars successfuly delivered!!')