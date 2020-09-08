names = {'Mary':10999, 'Sam':2111, 'Amy':9778, 'Tom':20245, 'Michael':27115, 'Bob':5887, 'Kelly':7855}

ret1 = sorted(names)
print(ret1)

def x0(x):
    return x[0]

def x1(x):
    return x[1]

ret2 = sorted(names.items(), key=x0)
print(ret2)

ret3 = sorted(names.items(), key = lambda x:x[0])
print(ret3)

ret4 = sorted(names.items(), key=x1)
print(ret4)

ret5 = sorted(names.items(), key = lambda x:x[1])
print(ret5)