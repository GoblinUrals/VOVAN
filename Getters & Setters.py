class Alien:
    def init(self, name, age):
        self.name = name
        self.age = age

    def repr(self):
        return "age {}, name {}, greeting {}".format(self.age, self.name, self.greeting)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, newvalue):
        self.__age = newvalue
        self.greeting = "Hello I come in peace...My name is {} and Im {} years old".format(
            self.name, self.age)

alien = Alien("LargeAndSlimy", 2500)

# alien.age = alien.age + 1
#
# print(alien) # TypeError: Alien() takes no arguments

Alien.age = 3700
print(alien.age)