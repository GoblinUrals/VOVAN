"""поиск слова в списке максимально непохожего на другие"""

import itertools
from random import randint

def find_uniq(arr):
    m = randint(0,len(arr)-1)
    # m = 3
    c = []
    print(m)
    for i in range(len(arr[m])):
        b = [arr[m][i] in list(x) for x in arr]
        # print(b)
        z = [i for i in range(len(b)) if b[i] == False]
        # print(z)
        c.append([i for i in range(len(b)) if b[i] == False])
    print(c)
    if c[0] == c[1] and len(c[0])==1:
        print('Whoy')
        qwerty = list(itertools.chain.from_iterable(c))
        return arr[max(qwerty, key=qwerty.count)]
    elif c[0] == c[1] :
        e = (c[0]+[m for m in range(c[0][0],c[0][-1]+1)])
        # print(e)
        q = [m for m in range(c[0][0], c[0][-1] + 1)].index(min(e, key=e.count))
        return arr[q]
    else:
        print('Whoy')
        qwerty = list(itertools.chain.from_iterable(c))
        return arr[max(qwerty, key=qwerty.count)]




# arr= [ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'aAaaA' ]
arr = [' ','a','   ']
# arr = [ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]

print(find_uniq(arr))



# 3
# [False, False, False, True, False, False, False]
# [0, 1, 2, 4, 5, 6]
# [False, False, False, True, False, False, False]
# [0, 1, 2, 4, 5, 6]
# [False, False, False, True, False, False, False]
# [0, 1, 2, 4, 5, 6]
# [False, False, False, True, False, False, False]
# [0, 1, 2, 4, 5, 6]
# [[0, 1, 2, 4, 5, 6], [0, 1, 2, 4, 5, 6], [0, 1, 2, 4, 5, 6], [0, 1, 2, 4, 5, 6]]
# [0, 1, 2, 4, 5, 6, 0, 1, 2, 4, 5, 6, 0, 1, 2, 4, 5, 6, 0, 1, 2, 4, 5, 6]
# Aa


# 5
# [True, False, False, False, True, True, True]
# [1, 2, 3]
# [True, True, True, False, True, True, True]
# [3]
# [True, False, False, False, True, True, True]
# [1, 2, 3]
# [True, True, True, False, True, True, True]
# [3]
# [True, False, False, False, True, True, True]
# [1, 2, 3]
# [True, True, True, False, True, True, True]
# [3]
# [[1, 2, 3], [3], [1, 2, 3], [3], [1, 2, 3], [3]]
# [1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3]
# BbBb
