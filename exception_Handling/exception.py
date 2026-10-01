
try:
    x=int(input('Enter x'))
   # y=int(input('Enter y'))
    y=input('Enter y')

    print(x/y)


except ZeroDivisionError:
    print('Zaro div erroe')

except ValueError:
    print('Value error')

except TypeError:
    print('type erroe')

except Exception as e :              # it will catch any error which is not mention
    print('Unknown error')


finally :
    print('Server is running')
    
