
def func():
    lst, lst_2 = ['Thank you'], [5,6,7]
    dict = {'Benjamin':'Python','Coach Computing':'Python','Mike':'Python','Rune':'Python'}
    return (dict.fromkeys(dict, lst))

print(func())
# {'Benjamin': ['Thank you'], 'Coach Computing': ['Thank you'],
# 'Mike': ['Thank you'], 'Rune': ['Thank you']}

