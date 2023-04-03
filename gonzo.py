a = ['hello','bears','west']

def func(x):
    a.extend(x)
    return a

x = 'boa'

y = ['boa']

print(func(x)) # ['hello', 'bears', 'west', 'b', 'o', 'a']
print(func(y)) # ['hello', 'bears', 'west', 'b', 'o', 'a', 'boa']

import random

d = random.choices(a)
print(d)