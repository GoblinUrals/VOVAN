q = ['A','B','C','S']
q_1 = ['a','a','b','c','c','s']

# f = []
# for i in q:
#     f.append(i)
#     for el in q_1:
#         if i.lower() == el:
#             f.append(el)

# print(f) # ['A', 'a', 'a', 'B', 'b', 'C', 'c', 'c', 'S', 's']

f = []
for i in q:
    f.append(i)
    f.append([el for el in q_1 if i.lower() == el])

print(f)
# ['A', ['a', 'a'], 'B', ['b'], 'C', ['c', 'c'], 'S', ['s']]

# [i for i in a if i.lower() != x else x for x in q_1 ]