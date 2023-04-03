q = ['A','B','C','S']
q_1 = ['a','a','b','c','c','s']

f = []
for i in q:
    f.append(i)
    for el in q_1:
        if i.lower() == el:
            f.append(el)
print(f) # ['A', 'a', 'a', 'B', 'b', 'C', 'c', 'c', 'S', 's']

# f = [el for el in q_1 if i.lower() == el and i for i in q]
# f =[]
# w = [f.append(el) for el in q_1 if i.lower()!= el else  f.append(i) for i in q]

# f = [el for i in q i for el in q_1 if i.lower() == el]

# f = [(el or i)for el in q_1 if i.lower() == el for i in q ]
# print(f)
# f = []
# z = [f.append(el) for el in q_1 if i.lower() != el else f.append(i) for i in q]

# z = [f.append(i) for i in q f.append(el) for el in q_1 if i.lower() == el ]
# z = [f.append(i) (f.append(el) for el in q_1 if i.lower() == el ) for i in q]
# print(z)

f = [el if i.lower() == el else i for el in q_1 for i in q]
print(f)
# ['a', 'B', 'C', 'S', 'a', 'B', 'C', 'S', 'A', 'b', 'C', 'S',
#  'A', 'B', 'c', 'S', 'A', 'B', 'c', 'S', 'A', 'B', 'C', 's']

f = [i if i.lower() != el else el for i in q for el in q_1]
print(f)
# ['a', 'a', 'A', 'A', 'A', 'A', 'B', 'B', 'b', 'B', 'B', 'B',
#  'C', 'C', 'C', 'c', 'c', 'C', 'S', 'S', 'S', 'S', 'S', 's']

f = [i if i.lower() != el else el for el in q_1 for i in q]
print(f)
# ['a', 'B', 'C', 'S', 'a', 'B', 'C', 'S', 'A', 'b', 'C', 'S',
#  'A', 'B', 'c', 'S', 'A', 'B', 'c', 'S', 'A', 'B', 'C', 's']