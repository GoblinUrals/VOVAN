from pathlib import Path

print(Path.cwd()) # C:\Users\Влад\PycharmProjects\PROBA\My_training

p = Path()
print(p) # .

print(p.resolve()) # C:\Users\Влад\PycharmProjects\PROBA\My_training

p = Path('zabava_2.py')
with p.open() as g:
    g.readline()

print(g) # <_io.TextIOWrapper name='zabava_2.py' mode='r' encoding='cp1251'>