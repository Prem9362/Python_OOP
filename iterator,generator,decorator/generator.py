def gp(st,end,step):
    value = st
    while value<end:
        yield(value)
        value=value*step

#it1=iter(gp(2,40,3))
#print(next(it1))
#print(next(it1))
#print(next(it1))

for i in gp(2,40,3):
    print(i)