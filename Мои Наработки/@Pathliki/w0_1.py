import pathlib
from pathlib import Path

p = pathlib.Path('/Users/Влад/Desktop/cox/live in dura.jpeg')

print(p.is_file())
p_1 = pathlib.Path('/Users/Влад/Desktop/cox/1.jpeg')

p.rename(p_1)

