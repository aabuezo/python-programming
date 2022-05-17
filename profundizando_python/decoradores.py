def decorador(funcion_decorada):
    def funcion_interna(*args, **kwargs):
        print('Antes de llamar a la funcion decorada')
        resultado = funcion_decorada(*args, **kwargs)  # aqui se llama
        print('Despues de llamar a la funcion decorada')
        return resultado

    return funcion_interna


@decorador
def sumar(a, b):
    return a + b


resultado = sumar(3, 5)
print(f'Resultado suma: {resultado}')
