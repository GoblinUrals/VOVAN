
# """определить индекс пропущенного  элемента в нарастающей прогрессии"""
# c =[1,2,3,5,6,7,8]
# # c = [0,2,3,4,5,6,7]
#
# e = (c+[m for m in range(c[0],c[-1]+1)])
#
# print([m for m in range(c[0],c[-1]+1)].index(min(e,key=e.count)))
# # 3
# print(len([1,2,3,4,5,6,7]))
# # 7
def function():
    return 'A function'


class Klass:
    def __init__(self):
        print('A constructor')

    def method(self):
        return 'A method'

    def __call__(self):
        return 'An object'


obj = Klass()
# A constructor
a_type = list

for callable_thing in [
    function,
    lambda:'Another function',
    Klass,
    obj.method,
    obj,
    a_type,
    ]: print(callable_thing())

# A function
# Another function
# A constructor
# <__main__.Klass object at 0x000000000247A6A0>
# A method
# An object
# []
