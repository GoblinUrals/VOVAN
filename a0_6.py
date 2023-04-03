from collections import deque

def func():
    names = deque(['John','Oscar','Faith'])
    names.append('Eric')
    names.append('David') # deque(['John','Oscar','Faith','Eric','David'])
    names.popleft()       # deque(['Oscar','Faith','Eric','David'])
    names = set(names)    # {'Faith','David','Eric','Oscar'}
    names.pop()
    return names

print(func()) # {'David','Eric','Oscar'}


def func_1():
    names = deque(['John','Oscar','Faith'])
    names.append('Eric')
    names.append('David') # deque(['John','Oscar','Faith','Eric','David'])
    print(names)
    names.popleft()       # deque(['Oscar','Faith','Eric','David'])
    print(names)
    names = frozenset(names)
    # names.pop()  # AttributeError
    return names

print(func_1()) # frozenset({''Eric','Oscar','Faith','David'})