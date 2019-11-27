def my_timer(orig_func):
    import time
    
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time()
        print("{} executed at {}".format(orig_func.__name__, t2-t1))
    return wrapper
    
@my_timer
def display_info(nome, age):
    print('display_info ran with arguments ({},{})'.format(nome, age))

display_info('wrtinho',10)
