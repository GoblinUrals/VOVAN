class Model:
    def __init__(self, name, version):
        self.name = name
        self.version = version

    def __repr__(self) -> str:
        return f"Model(name = '{self.name}' version = '{self.version}')"

    def __eq__(self, other) -> bool:
        return self.name == other.name and self.version == other.version


m1 = Model("Vlad", "v1")
m2 = Model("Mary", "v2")

print(m1)            # Model(name = 'Vlad' version = 'v1')
print(m2)            # Model(name = 'Mary' version = 'v2')
print(m1.__eq__(m2)) # False
print(m1.__eq__(m1)) # True

