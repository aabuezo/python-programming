# Docstring
class MiClase:
    '''
    Ejemplo de documentacion de MiClase
    '''
    def __init__(self):
        '''
        Metodo de inicio de MiClase
        '''
    def mi_metodo(self, param1, param2):
        '''
        PyCharm agrega automaticamente los parametros al docstring
        :param param1:
        :param param2:
        :return:
        '''


# help(MiClase)
# print(MiClase.__doc__)
# print(MiClase.__init__.__doc__)
print(MiClase.mi_metodo.__doc__)

