
class Data:

    def __matmul__(self, other):
        return '... my result of matmul...'


a = Data()
b = Data()
c = a @ b
print(c)


# ... my result of matmul...


class Peak:

    def __matmul__(self, value):
        print(f"Using{value!r}")
        return value

p = Peak()

def add7(a, b):
    return a + b +7

z = [p@"Look:", p@add7(p@10, p@20)]
print(z)