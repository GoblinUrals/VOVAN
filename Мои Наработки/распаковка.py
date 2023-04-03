# ________________________________________________________
print([x for x in "Hello World!" if x.isupper()])
# ['H', 'W']
print(*[x for x in "Hello World!" if x.isupper()])
# H W
print(*(x for x in "Hello World!" if x.isupper()))
# H W
# __________________________________________________________

a, b, c = [1,2,3], (4,5,6), {7,8,9}

print([*a, *b, *c]) # [1, 2, 3, 4, 5, 6, 8, 9, 7]

d = {'a':1,'b':2,'c':3,'d':4,'e':5}

print(*d) # a b c d e
# _________________________________________________________

print(*[x.upper() for x in 'I am python developer'])
# I   A M   P Y T H O N   D E V E L O P E R
# _________________________________________________________

print(type(*['1'])) # <class 'str'>
print(type([1])) # <class 'int'>
print(type((100,))) # <class 'tuple'>
# _________________________________________________________

print(*"abcdefg") # a b c d e f g
# ___________________________________________________________

a = {"w": 5, "x": 6}
b = {"y": 7}
c = {"z": 8, **a, **b}

print(c) # {'z': 8, 'w': 5, 'x': 6, 'y': 7}
# ____________________________________________________________

names = ['yAnG', 'MASk', 'thoMas', 'LISA']

print('{} {} {} {}'.format(*names))
# yAnG MASk thoMas LISA

print(('{} ' * len(names)).format(*names))
# yAnG MASk thoMas LISA
# _____________________________________________________________