x = 123
print(locals())
print()
print(globals())


def func(a=1):
    x = 234
    y = 111
    print(locals())
    print()
    print(globals())

    def func_y(c=2):
        x = 234
        z = 222
        print(locals())
        print()
        print(globals())
        return x

    func_y()
    return x


func()

# {'__name__': '__main__', '__doc__': None, '__package__': None,
#  '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000000000041F8E0>,
# '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>,
# '__file__': 'C:\\Users\\Влад\\PycharmProjects\\VOVAN\\a0_1.py', '__cached__': None, 'x': 123}

# {'__name__': '__main__', '__doc__': None, '__package__': None,
#  '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000000000041F8E0>,
# '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>,
# '__file__': 'C:\\Users\\Влад\\PycharmProjects\\VOVAN\\a0_1.py', '__cached__': None, 'x': 123}

# {'a': 1, 'x': 234, 'y': 111}

#'__name__': '__main__', '__doc__': None, '__package__': None,
# '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x00000000004BF8E0>,
# '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>,
# '__file__': 'C:\\Users\\Влад\\PycharmProjects\\VOVAN\\a0_1.py', '__cached__': None,
# 'x': 123, 'func': <function func at 0x0000000001DDA550>}

# {'c': 2, 'x': 234, 'z': 222}

# {'__name__': '__main__', '__doc__': None, '__package__': None,
#  '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x00000000004BF8E0>,
# '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>,
# '__file__': 'C:\\Users\\Влад\\PycharmProjects\\VOVAN\\a0_1.py', '__cached__': None,
# 'x': 123, 'func': <function func at 0x0000000001DDA550>}
