"""Подсчитать число букв в строке малого регистра
при чем вывести только число букв выше 1"""
import re

def func(s: str):
    x = ''.join(re.findall(r'[a-z]',s))
    y = {i:x.count(i) for i in x.lower()}
    print(y)
    z = [f"{v}:{k*v}/" for k,v in y.items() if v > 1]
    z.sort(key=lambda x:x.split(':')[1],reverse=True)
    q = re.sub(r'\d','1',''.join(z))
    return (q)

s = "Sadus:cpms>orqn3zecwGvnznSgacs"
# s = 'codewars'
# s = "& aaa bbb c d"
# s = "A generation must confront the looming "
print(func(s))
# "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr"

# {'h': 1, 'a': 4, 't': 3, 'c': 1,
#  'n': 2,'i': 1, 'd': 3, 'o': 5,
# 'y': 1, 'm': 1, 'r': 2, 'w': 1}

# ['4/: aaaa', '3/: ddd', '2/: nn',
# '5/: ooooo', '2/: rr', '3/: ttt']