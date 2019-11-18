def method_require(register):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if register == 'upper':
                return func(*args, **kwargs).upper()
            elif register == 'lower':
                return func(*args, **kwargs).lower()
            raise Exception('Wrong')
        return wrapper
    return decorator


@method_require('upper')
def foo():
    return 'SdasSADasdas'


print(foo())
