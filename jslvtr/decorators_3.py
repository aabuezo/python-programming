import functools


user = {
    'id': 1,
    'username': 'ale',
    'access_level': 'admin'
}


def user_has_permission(access_level):
    def my_decorator(func):
        @functools.wraps(func)  # para que func mantenga __name__ y __doc__
        def secure_func(*args, **kwargs):   # generic
            if user.get('access_level') == access_level:
                return func(*args, **kwargs)    # generic
            else:
                raise PermissionError('You are not admin.')
        return secure_func
    return my_decorator


@user_has_permission('admin')
def my_function(panel):
    return f'Password for panel {panel} is 1234'
# my function = user_has_permission('admin')(my_function)


print(my_function('movies'))
print(my_function.__name__)
print(my_function.__doc__)
