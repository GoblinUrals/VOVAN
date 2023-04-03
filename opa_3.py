
s = {'a':1,'b':2,'c':3,'d':4,'e':5}

n = list()
for key,val in s.items():
    n.append((val,key))
n.sort(reverse=True)

print(n)
# [(5, 'e'), (4, 'd'), (3, 'c'), (2, 'b'), (1, 'a')]

def myfunc(a):
    empty = []
    for i in range(len(a)):
        if i % 2 == 0:
            empty.append(a[i].upper())
        else:
            empty.append(a[i].lower())

    return "".join(empty)

print(myfunc("abcdef"))
# 'AbCdEf'
print(myfunc("ABCDEF"))
# 'AbCdEf'
print(myfunc("A CDEF"))
# 'A CdEf'

def myfunc(a):
    return "".join([c.lower() if inx % 2 == 0 else c.upper()
                    for inx, c in enumerate(a)])

for i in ['abcdef','ABCDEF','A CDEF']:
    print(myfunc(i))

# aBcDeF
# aBcDeF
# a cDeF

def myfunc(a):
    return "".join([c.lo() if inx % 2 else c.up()
                    for inx, c in enum(a)])

for i in ['abcdef','ABCDEF','A CDEF']:
    print(myfunc(i))

# aBcDeF
# aBcDeF
# a cDeF