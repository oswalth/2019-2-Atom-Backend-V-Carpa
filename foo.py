import time


def my_cache(func):
    def my_wrapper(n):
        res = func(n)
        if n in cache_dict.keys():
            return cache_dict[n]
        cache_dict[n] = res
        return res
    return my_wrapper
        

cache_dict = dict()
@my_cache
def fibonacci(n):
    assert n >= 0
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


ts = time.time()
fibonacci(30)
print(time.time() - ts)