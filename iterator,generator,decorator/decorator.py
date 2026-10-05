def decorator(f):
    def inner():
        print('Welcome to')
        f()
        print("!!!!!!!!!!")
    return inner


@decorator
def f1():
    print('Mumbai')

def f2():
    print('Pune')    

f1()
f2()