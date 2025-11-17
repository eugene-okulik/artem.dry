def decor(func):
    def wrapper():
        func()
        print('finished')
    return wrapper


@decor
def func2():
    print('hello')


func2()
