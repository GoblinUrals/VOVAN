
from itertools import groupby

for key,group in groupby('Pyttthhhonnnnnist'):
    print(key, list(group))

# P ['P']
# y ['y']
# t ['t', 't', 't']
# h ['h', 'h', 'h']
# o ['o']
# n ['n', 'n', 'n', 'n', 'n']
# i ['i']
# s ['s']
# t ['t']

import  itertools

result = itertools.islice('ABCDEFG',0,None,3)
for item in result:
    print(item,end = ' ')
#A D G