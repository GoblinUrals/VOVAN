class Phone:

    def __init__(self, brand, model, year, name):
        self.brand = brand
        self.model = model
        self.year = year
        self.name = name

    def receive_call(self):
        return (f"Звонит {self.name}")

    def get_info(self):
        return (self.brand, self.model, self.year)

    def __str__(self):
        return (f"Брэнд: {self.brand},\nМарка: {self.model},\nГод выпуска: {self.year}")


brand, model, year, name = 'Samsung', 'F200', '2015', 'Vlados'
r = Phone(brand, model, year, name)
print(r, '\n')
print(r.receive_call(), '\n')
print(r.get_info())

# OUTPUT:
# Брэнд: Samsung,
# Марка: F200,
# Год выпуска: 2015

# Звонит Vlados

# ('Samsung', 'F200', '2015')
# __________________________________________________________________________________________

"""Закодировать и раскодировать слово со сменщением shift"""


class CaesarCipher(object):
    def __init__(self, shift):
        self.shift = shift

    def encode(self, st):
        st_u = list(st)
        for i in range(len(st_u)):
            inx = str_u.index(st_u[i].upper())
            if inx + self.shift > len(str_u):
                st_u[i] = str_u[(inx + self.shift - len(str_u))]
            else:
                st_u[i] = str_u[inx + self.shift]
        return ''.join(st_u)

    def decode(self, st):
        st_u = list(st)
        for i in range(len(st_u)):
            inx = str_u.index(st_u[i])
            if (inx - self.shift) < 0:
                st_u[i] = str_u[(inx - self.shift + len(str_u))]
            else:
                st_u[i] = str_u[inx - self.shift]
        return ''.join(st_u)


# shift-смещение

str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

str_u = list(str)

c = CaesarCipher(5)

print(c.encode('Codewars'))
print(c.decode('HTIJBFWX'))
# ___________________________________________________________________________
