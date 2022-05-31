import time
import math


def sumar_digitos(n):
    car = str(n)
    if len(car) == 1:
        return int(car)
    else:
        return sumar_digitos(int(car[0]) + int(car[1:]))


# leer el archivo de la criba
with open('criba.txt', 'r') as file:
    print(f'Leyendo el archivo: {file}')
    cad = file.read()
    criba = cad.split(',')
    criba.pop()
    print('Se cargo la criba en memoria.')
    # print(f'criba: {criba}')


# criba = [False]     # 0 no es primo

def is_prime_criba(n):
    try:
        if criba[n] == True:
            return True
    except Exception as e:  # n not in criba
        print(f'criba[{n}]: {criba[n]}')
    finally:
        if (n != 2 and n % 2 == 0):
            criba.append(False)
            return False
        else:
            a = math.floor(n ** .5)
            for i in range(3, a + 1):  # 2 ya fue descartado arriba
                if (n % i == 0):
                    # print(f'n: {n}, i: {i}, n/i: {n/i}')
                    criba.append(False)
                    return False
        criba.append(True)
        return True


def is_prime(n):
    if (n != 2 and n % 2 == 0):
        return False
    else:
        a = math.floor(n ** .5)
        for i in range(3, a + 1):  # 2 ya fue descartado arriba
            if (n % i == 0):
                # print(f'n: {n}, i: {i}, n/i: {n/i}')
                return False
    return True


def llenar_criba(n):
    for i in range(1, n):   # 2 ya fue descartado arriba
        if is_prime(i):
            criba.append(i)
    print('Done.')

# print(reducir_digitos(1))
# print(reducir_digitos(19))
# print(reducir_digitos(1111))

# cargar criba hasta 10M y guardar en un archivo
# criba = []
# print('Se comienza a cargar la criba...')
# start = time.time()
# for i in range(1, 100):
#     if is_prime(i):
#         criba.append(True)
#     else:
#         criba.append(False)
# end = time.time()
# print('Fin carga criba.')
# print(f'tiempo: {end - start}')
#
# with open('criba.txt', 'a') as file:
#     print(f'Guardando la criba en {file}')
#     for item in criba:
#         file.write(str(item)+',')
#     print('se guardo el archivo.')

lst_max = [100, 1000, 10000, 100000]
# lst_max = [100]
# suma_digitos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# ultimos_digitos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for max in lst_max:
    start = time.time()

    count = 0
    for n in range(1, max):
        if (is_prime_criba(n)):
            count += 1
            # digito_suma = sumar_digitos(n)
            # ultimo_digito = int(str(n)[-1])
            # print(n, ultimo_digito, digito_suma)
            # suma_digitos[digito_suma] += 1
            # ultimos_digitos[ultimo_digito] += 1
    print(f'total: {count} prime numbers in {max} numbers. That\'s {count / max * 100} percent.')

    end = time.time()
    print(f'time: {end - start}')
    print()

# print(f'la criba tiene: {len(criba)} valores')
# print(criba)
# print(criba[3] and True)

#     print('digito\tultimo\tsuma')
#     for i in range(0, 10):
#         # print(f'{i}:\t{ultimos_digitos[i]}')
#         print(f'{i}:\t{ultimos_digitos[i]}\t{suma_digitos[i]}')


# print(math.log2(2**2046)) # es 2046...
# print(2**2048)
# print(f'{len(str(2**2048))} caracteres')
# bytes = 2**1024/8
# print(f'{bytes} bytes')
# print(f'{bytes/1024} Kbytes')
# print(f'{bytes/1024/1024} Mbytes')
# print(f'{bytes/1024/1024/1024} Gbytes')

# print(2**512)
# print(f'len(str(2**512)) caracteres')
# print(10**155)

# print(10**78)
# print(10**78/(1024**3))
# print((10**308)*0.05)
