import functools


user = {
    'id': 1,
    'username': 'ale',
    'access_level': 'admin'
}


# este decorador solo sirve para la funcion que le pasa el parametro
def user_has_permission(func):
    @functools.wraps(func)  # para que func mantenga __name__ y __doc__
    def secure_func(panel):
        if user.get('access_level') == 'admin':
            return func(panel)
        else:
            raise PermissionError('You are not admin.')
    return secure_func


@user_has_permission
def my_function(panel):
    return f'Password for panel {panel} is 1234'


@user_has_permission
def another():
    pass


print(my_function('movies'))
print(another())
