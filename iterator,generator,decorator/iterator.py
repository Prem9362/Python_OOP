a=[10,3.14,'prem']
it1=iter(a)

try:
    print(next(it1))
    print('HI!')
    print(next(it1))
    print("hello")
    print(next(it1))
    print('OOOO!!!!')
    print(next(it1))

except StopIteration :
    print("StopIteration Error")
print('Server is running')
