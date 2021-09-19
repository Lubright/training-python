
class A:
    """有風險的寫法
    """
    def __init__(self) -> None:
        pass

    def set_name(self, name):
        self.name = name
    
    def set_age(self, age):
        self.age = age

    def __str__(self):
        return "{} my name is {}, I'm {} years old.".format(self.__class__.__name__, self.name, self.age)

a = A()
a.set_name("Python")
a.set_age(27)

print(a)

print("-" * 50 + "\n")

class B:
    """正確的寫法
    """
    def __init__(self, name, age) -> None:
        # 初始化實例屬性
        self.name = name
        self.age = age
    
    def set_name(self, name):
        self.name = name
    
    def set_age(self, age):
        self.age = age

    def __str__(self):
        return "{} my name is {}, I'm {} years old.".format(self.__class__.__name__, self.name, self.age)


b = B("Python", 27)
print(b)

print("-" * 50 + "\n")

class C:
    name = "Python"
    age = 27

    def __init__(self) -> None:
        pass

    def __str__(self):
        return "{} my name is {}, I'm {} years old.".format(self.__class__.__name__, C.name, C.age)

c = C()
print(c)

print("-" * 50 + "\n")