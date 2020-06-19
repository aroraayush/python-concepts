def mylogger(func):
    def wrapper(*args, **kwargs):
        print(f'=== Running "{func.__name__}()" from Decorator ===')
        return func(*args, **kwargs)
    return wrapper

@mylogger
def add(a,b):
    """Doc string of function add

    Args:
        a (int): Number 1
        b (int): Number 2
    """
    return a + b

add(1,2)
print('add.__name__ = ', add.__name__) # decorator function's name
print('add.__doc__ = ', add.__doc__)   # decorator function's doc