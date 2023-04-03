class Dog:
    """Это класс Dog"""
    kind = "canine"

    def __init__(self):
        self.name = None

    def greet(self):
        print('Слава России!')


"""Создаем объекты класса Dog"""
d, e = Dog('Fido'), Dog('Buddy')

"""Атрибут класса Dog"""
print(Dog.kind)  # canine

"""Атрибуты объекта класса Dog"""
print(d.kind, e.kind)  # canine canine

print(Dog.greet)
# <function Dog.greet at 0x01B3E2F8>

print(d.name)  # Fido
print(e.name)  # Buddy

# print(Dog.greet()) # AttributError

"""Вызов метода объекта класса Dog"""
print(d.greet())  # Слава России!

print(e.greet)
# <bound method Dog.greet of <main.Dog object at 0x004861C0>>
