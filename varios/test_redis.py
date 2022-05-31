import redis
import time


r = redis.Redis(host='localhost', port=6379)
r.set('France', 'Paris')
r.set('Argentina', 'Buenos Aires')

capitals = []
capitals.append(r.get('France'))
capitals.append(r.get('Argentina'))

print(f'France: {capitals[0]}')
print(f'Argentina: {str(capitals[1])}')

r.mset({'Germany': 'Berlin', 'Peru': 'Lima'})
print(f'Germany: {r.get("Germany")}')
print(f'Peru: {r.get("Peru")}')

if (r.exists('Serbia')):
    print(r.get('Serbia'))
else:
    print('Cannot get the capital. Getting from API')

r.psetex('Uruguay', 1000, 'Montevideo') # vive por 1 seg..
print(f'Uruguay: {r.get("Uruguay")}')
time.sleep(2)
print(f'Uruguay: {r.get("Uruguay")}')   

