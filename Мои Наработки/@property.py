# ______________________________________________________________________
"""Персональный данные человека с возможностью коррекции даты рождения"""

class Person:
    def __init__(self, name, birth_day):
        self.name = name
        self._birth_day = birth_day

    def get_birth_day(self):
        return self._birth_day

    def set_birth_day(self, value, force=False):
        if force:
            self._birth_day = value
        else:
            raise AttributeError("Can't set birth_day")


man = Person('Vlad','02_02_1973')

print(man.get_birth_day())
# 02_02_1973

# """Установка новой даты рождения заблокирована"""
# print(man.set_birth_day('23_02_1973'))
# # AttributeError: Can't set birth_day

"""Снимаем блокировку через force=True"""
print(man.set_birth_day('23_02_1973', force=True))
# None

"""Показываем обновленную дату рождения"""
print(man.get_birth_day())
# 23_02_1973
# _____________________________________________________________________