a = [1,5,3,6,3,5,6,1]
b = []
for i in a:
    if i not in b:
        b.append(i)
print(b) # [1, 5, 3, 6]

b = []
w = [b.append(x) for x in a if x not in b]# [None, None, None, None]
print(w)

nums = [4, 1, 2, 1, 2]

