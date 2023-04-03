"""Вывод только тех слов списка names чья последняя буква после 'm'"""

names = ['Alex', 'Ben', 'Cait', 'Dan', 'Esther',
         'Frank', 'Geoff', 'Harry', 'Ian', 'jim'
         ]


def func(name):
    print(name)
    return name[-1] > 'm'


all(func(name) for name in names)

# Alex
# Ben
# Cait
# Dan
# Esther
# Frank
# ____________________________________________________________________________

w = (['x','y'],)
print(w[0]) # ['x','y']
q  = w[0].__iadd__(['z'])
print(q) # ['x','y','z']