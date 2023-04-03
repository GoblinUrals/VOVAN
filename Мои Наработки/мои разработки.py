"""Определить минимальную длинну слова в строке"""
def find_short(s):
    return (min(map(lambda x:len(x), s.split())))

s = "bitcoin take over the world maybe who knows perhaps"
print(find_short(s))
# 3
# ___________________________________________________________________
def high_and_low(numbers):
    a = max(int(x) for x in numbers.split())
    b = min(int(x) for x in numbers.split())
    numbers = str(a)+str(b)
    return numbers

numbers = "8 3 -5 42 -1 0 0 -9 4 7 4 -4"

print (high_and_low(numbers))
# 42-9
# ______________________________________________________________________________
"""Определить значение которое чаще всех"""

qwerty = [[0, 3], [1, 2, 3], [0, 3], [0, 3], [1, 2, 3]]

asd_ = max(qwerty, key=qwerty.count)
print(asd_)
#[0,3]

# a = ['hello', '2', 'text', '4', '5', '[list]', '9']

a = ["'hello'", '2', "'text'", '4', '5', "'[list]'","'9'"]
print(a)
#["'hello'", '2', "'text'", '4', '5', "'[list]'", "'9'"]

b = [2, 4, 5, '9', 'hello', 'text', '[list]']
c = [int(a[i]) if a[i].isdigit() else str(a[i]).strip("'") for i in range(len(a))]
print(c)
#['hello', 2, 'text', 4, 5, '[list]', '9']
# ________________________________________________________________________________

"""Подсчитать число букв в строке малого регистра
при чем вывести только число букв выше 1"""
import Регулярка

def func(s: str):
    x = ''.join(re.findall(r'[a-z]',s))
    y = {i:x.count(i) for i in x.lower()}
    print(y)
    z = [f"{v}/: {k*v}" for k,v in y.items() if v > 1]
    z.sort(key=lambda x:x.split(':')[1])
    return z

# s = "& aaa bbb c d"
s = "What can i do  today and tomorrow"
print(func(s))
# --------------------------------------------------------------------------------
"""определить индекс пропущенного  элемента в нарастающей прогрессии"""
c =[1,2,3,5,6,7,8]
# c = [0,2,3,4,5,6,7]

e = (c+[m for m in range(c[0],c[-1]+1)])

print([m for m in range(c[0],c[-1]+1)].index(min(e,key=e.count)))
# 3
print(len([1,2,3,4,5,6,7]))
# 7
# --------------------------------------------------------------------------------