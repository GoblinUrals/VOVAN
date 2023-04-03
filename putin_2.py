
def func(x):
    d = []
    for i in x:
        if isinstance(i, list):
            d += func(i)
        else:
            d.append(i)
    return d

a = [[1,[1,2,3,4],3,4],[5,6,7,8]]
print(func(a))
