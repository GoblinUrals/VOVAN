import itertools
from random import randint

def find_uniq(arr):
    m = randint(0,len(arr)-1)
    # m = 6
    print(m)
    num = []
    for i in range(len(arr[m])):
        b = [arr[m][i] in list(x) for x in arr]
        print(b)
        num.append([b.index(min(b, key=b.count))])
    print(num)
    r = list(itertools.chain.from_iterable(num))
    return arr[(max(r, key=r.count))]





arr = [ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'aAaaA' ]
# arr = [' ','a','  ']
# arr = [ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]
print(find_uniq(arr))

# m='foo'
# [False, False, False, True, False, False, False]
# [[0, 1, 2, 4, 5, 6]]
# [False, False, False, True, False, False, False]
# [[0, 1, 2, 4, 5, 6], [0, 1, 2, 4, 5, 6]]
# [False, False, False, True, False, False, False]
# [[0, 1, 2, 4, 5, 6], [0, 1, 2, 4, 5, 6], [0, 1, 2, 4, 5, 6]]
# [0, 1, 2, 4, 5, 6, 0, 1, 2, 4, 5, 6, 0, 1, 2, 4, 5, 6]
# abc


#
# m='bac'
# [True, True, True, False, True, True, True]
# [[3]]
# [True, True, True, False, True, True, True]
# [[3], [3]]
# [True, True, True, False, True, True, True]
# [[3], [3], [3]]
# [3, 3, 3]
# foo




















