import functools


user = {
    'id': 1,
    'username': 'ale',
    'access_level': 'admin'
}


def user_has_permission(func):
    @functools.wraps(func)  # para que func mantenga __name__ y __doc__
    def secure_func():
        if user.get('access_level') == 'admin':
            return func()
        else:
            raise PermissionError('You are not admin.')
    return secure_func


@user_has_permission
def my_function():
    """
    Allows us to login as admin
    :return:
    """
    return 'Access granted.'


print(my_function())
print(my_function.__name__)
print(my_function.__doc__)

