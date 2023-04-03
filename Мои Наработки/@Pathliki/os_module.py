import os
from os.path import isfile, join

"""В каком текущем каталоге находимся"""
print(os.getcwd())
# C:\Users\Влад\PycharmProjects\Guru\мои наработки\@Deathlike

"""Меняем название текущего каталога на 'rondo'"""
# os.chdir('rondo')

"""Список файлов  и папок текущего каталога"""
print(os.listdir('.'))
# ['a1.py', 'a2.py', 'a2_0.py']

print(os.getlogin())
# Влад

"""Идентификатор текущего процесса"""
print(os.getpid())
# 2488

"""Раскрываем генератор дерева каталогов и файлов os.walk()."""
for dir_path, dir_names, file_names in os.walk('.'):

    for dir_name in dir_names:
        print("Каталог :", os.path.join(dir_path, dir_name))

    for file_name in file_names:
        print("Файл :", os.path.join(dir_path, file_name))

# Файл : .\a1.py
# Файл : .\a2.py
# Файл : .\a2_0.py
# _________________________________________________________________

p = '/Users/Влад/Desktop/html'

"""Просматриваем состав папки /html"""
print(os.listdir(p))
# ['allure.jpg', 'databases.db', 'django.txt', 'index.html',
# 'my foto.jpg', 'my_foto2.jpg', 'sally']

"""Просматриваем только файлы из папки /html"""
files = [f for f in os.listdir(p) if isfile(join(p, f))]
print(files)
# ['allure.jpg', 'databases.db', 'djago.txt', 'index.html',
# 'my foto.jpg', 'my_foto2.jpg']
# ___________________________________________________________________

"""Указываем путь и имя создаваемой папки ,
 и в папке /html создается папка mambos """
os.mkdir('/Users/Влад/Desktop/html/mambos', mode=0o777)

"""Чтобы избежать ошибки повторным созданием той же папки /mambos"""
if not os.path.isdir('mambos'):
    os.mkdir('/Users/Влад/Desktop/html/mambos')

"""Удаляем эту же папку"""
os.rmdir('/Users/Влад/Desktop/html/mambos')

"""Создаем в папке /html папку sally а в ней папки gotcha и Yuki"""
os.makedirs('/Users/Влад/Desktop/html/sally/gotcha/Yuki')

"""Удаляем эти папки из /html"""
os.removedirs('/Users/Влад/Desktop/html/sally/gotcha/Yuki')
# _____________________________________________________________________

"""Переименовываем папку /html в /harass .
Вторым путем указываем папку /harass ,
 где она должна быть находиться вместо /html"""
os.rename('/Users/Влад/Desktop/html', '/Users/Влад/Desktop/harass')
# _______________________________________________________________________

print(os.walk('.'))  # <generator object walk at 0x01368DB8>

"""Раскрываем генератор дерева каталогов и файлов папки /html"""
for dir_path, dir_names, file_names in os.walk(p):

    for dir_name in dir_names:
        print("Каталог :", os.path.join(dir_path, dir_name))

    for file_name in file_names:
        print("Файл :", os.path.join(dir_path, file_name))

# Каталог : /Users/Влад/Desktop/html\sally
# Файл : /Users/Влад/Desktop/html\allure.jpg
# Файл : /Users/Влад/Desktop/html\databases.db
# Файл : /Users/Влад/Desktop/html\django.txt
# Файл : /Users/Влад/Desktop/html\index.html
# Файл : /Users/Влад/Desktop/html\my foto.jpg
# Файл : /Users/Влад/Desktop/html\my_foto2.jpg
# Каталог : /Users/Влад/Desktop/html\sally\gotcha
# Каталог : /Users/Влад/Desktop/html\sally\gotcha\Yuki

# __________________________________________________________________________

"""Информация о файле"""
print(os.stat('/Users/Влад/Desktop/html/allure.jpg'))
# os.stat_result(st_mode=33206, st_ino=22236523160276267, st_dev=981633409,
# st_link=1, st_uid=0, st_gid=0, st_size=197601, st_time=1652539738,
# st_time=1650196888, st_cti

"""Размер файла , в байтах"""
print(os.stat('/Users/Влад/Desktop/html/allure.jpg').st_size)
# 197601
print(os.stat('/Users/Влад/Desktop/html/databases.db').st_size)
# 0
print(os.stat('/Users/Влад/Desktop/html/django.txt').st_size)
# 311
# __________________________________________________________________________
"""Проверяем доступ у текстовому файлу"""


# os.F_OK - проверка существования файла или каталога,
# os.R_OK - проверка возможности чтения,
# os.W_OK - проверка возможности записи,
# os.X_OK - проверка выполнения файла или открытия директории

def func(__file__):
    print('Testing:', __file__)
    print('Exists:', os.access(__file__, os.F_OK))
    print('Readable:', os.access(__file__, os.R_OK))
    print('Writable:', os.access(__file__, os.W_OK))
    print('Executable:', os.access(__file__, os.X_OK))


p_1 = r'\Users\Влад\Desktop\html\django.txt'

func(p_1)
# Testing: \Users\Влад\Desktop\html\django.txt
# Exists: True
# Readable: True
# Writable: True
# Executable: True
# ______________________________________________________________
"""Некоторые комманды управления системой"""
list_command = ['notepad', 'date', 'shutdown -s']

print([os.system(cmd) for cmd in list_command])

# 1.Откроется блокнот и появится возможность там что-то написать
# 2.Откроется коммандная строка и выведется дата :
# ������ ���: 27.03.2023
# 3.Выключится компьютер
# _______________________________________________________________________
"""Имя операционной системы"""
print(os.name)  # nt
