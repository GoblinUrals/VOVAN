import re

string = 'For the sake of this video ,let is pretend this log file is thousand'
string2 = 'vlad.avto@mail.ru'

downo = re.findall(r'\b[\w+]', string)
print(downo)

# ['F', 't', 's', 'o', 't', 'v', 'l', 'i', 'p', 't', 'l', 'f', 'i', 't']
downo1 = re.findall(r'\w+', string)
print(downo1)

# ['For', 'the', 'sake', 'of', 'this', 'video', 'let', 'is', 'pretend', 'this', 'log', 'file', 'is', 'thousand']
downo2 = re.findall(r'([\w+.])', string)
print(downo2)

# ['F', 'o', 'r', 't', 'h', 'e', 's', 'a', 'k', 'e', 'o', 'f', 't', 'h', 'i', 's',
# 'v', 'i', 'd', 'e', 'o', 'l', 'e', 't', 'i', 's', 'p', 'r', 'e', 't', 'e', 'n',
# 'd', 't', 'h', 'i', 's', 'l', 'o', 'g', 'f', 'i', 'l', 'e', 'i',
# 's', 't', 'h', 'o', 'u', 's', 'a', 'n', 'd']
downo3 = re.findall(r'\b(\w+ )', string)
print(downo3)

# ['For ', 'the ', 'sake ', 'of ', 'this ', 'video ', 'let ', 'is ', 'pretend ', 'this ', 'log ', 'file ', 'is ']

# ___________________________________________________________________________________________________________

string = 'vlad.avto@mail.ru'

s = re.findall(r'@(\w+).(\w+)', string)
print(s)

data = [1, 2, 3, 4, -5, -6]

data_i = [i for i in range(0, len(data)) if data[i] > 0]

print(list(data_i))
# _______________________________________________________________________