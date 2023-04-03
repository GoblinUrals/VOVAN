def func(**kwargs):
    result = ""
    for i in kwargs.values():
        result += i
    return result

# print(func(a="Real", b="Python", c="Is", d="Great", e="!"))

kwargs = {"a":"Real", "b":"Python", "c":"Is" , "d":"Great", "e":"!"}

print(func(**kwargs))

"""Выбор рабочих дней"""

days = [d for d in range(1,32)]
print(days)
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
# 12, 13,14, 15, 16, 17, 18, 19, 20,
# 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

"""Делим список дней на недели"""

weeks = [days[i:i+7] for i in range(0, len(days), 7)]
print(weeks)
# [[1, 2, 3, 4, 5, 6, 7],
#  [8, 9, 10, 11, 12, 13, 14],
#  [15, 16, 17, 18, 19, 20, 21],
#  [22, 23, 24, 25, 26, 27, 28],
#  [29, 30, 31]]

"""Только рабочие дни по неделям"""

work_weeks = [week[0:5] for week in weeks]
print(work_weeks)
# [[1, 2, 3, 4, 5],
#  [8, 9, 10, 11, 12],
#  [15, 16, 17, 18, 19],
#  [22, 23, 24, 25, 26],
#  [29, 30, 31]]

"""Рабочие дни одним списком"""

wdays = [item  for sublist in work_weeks for item in sublist]
print(wdays)
#[1, 2, 3, 4, 5, 8, 9, 10, 11,
# 12, 15, 16, 17, 18, 19, 22,
# 23, 24, 25, 26, 29, 30, 31]

