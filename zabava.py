from functools import singledispatch

@singledispatch
def add(a, b):
    raise NotImplementedError('Неподдерживаемый тип')

@add.register(int)
def _(a, b):
    print("Первый аргумент имеет тип ", type(a))
    print(a + b)

@add.register(str)
def _(a, b):
    print("Первый аргумент имеет тип ", type(a))
    print(a + b)

@add.register(list)
def _(a, b):
    print("Первый аргумент имеет тип ", type(a))
    print(a + b)

if __name__ == "__main__":
    add(1, 2)
    add('Vlad', 'Strukov')
    add([1,2,3], [4,5,6])
    #NotImplementedError: Неподдерживаемый тип

# Первый аргумент имеет тип  <class 'int'>
# 3
# Первый аргумент имеет тип  <class 'str'>
# VladStrukov
# Первый аргумент имеет тип  <class 'list'>
# [1, 2, 3, 4, 5, 6]


from functools import singledispatch

@singledispatch
def func(arg):
    print(f"Object:{arg}")

@func.register(int)
def _func(arg):
    print(f"int: {arg}")

@func.register(str)
def _func(arg):
    print(f"str: {arg}")


@func.register(list)
def _func(arg):
    print(f"list: {arg}")

func((1,3,4,7)) # Object:(1, 3, 4, 7)
func(1)         # int: 1
func('Vlad')    # str: Vlad
func([1,2,4,5]) # list: [1, 2, 4, 5]

