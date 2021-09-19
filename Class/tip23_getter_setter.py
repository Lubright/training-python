class A:
    def __init__(self, *args, **kwargs) -> None:
        if len(args) == 0:
            self.__name = kwargs.get("name", "")
            self.__age = kwargs.get("age", 27)
        elif len(args) == 1:
            self.__name = args[0]
            self.__age = kwargs.get("age", 27)
        else:
            self.__name, self.__age = args
    
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age

    def __str__(self) -> str:
        return "[{}] name = {}, age = {}".format(
            self.__class__.__name__,
            self.__name,
            self.__age
        )

a = A(name="Python", age=27)

print(a)

print(a.get_name()) # 有點麻煩

print("-" * 50 + "\n")

class B:
    def __init__(self, *args, **kwargs) -> None:
        if len(args) == 0:
            self.__name = kwargs.get("name", "")
            self.__age = kwargs.get("age", 27)
        elif len(args) == 1:
            self.__name = args[0]
            self.__age = kwargs.get("age", 27)
        else:
            self.__name, self.__age = args

    
    # 得到 get
    @property
    def name(self):
        return self.__name
    
    @property
    def age(self):
        return self.__age

    # 得到 set
    @age.setter
    def age(self, age):
        self.__age = age

    def __str__(self) -> str:
        return "[{}] name = {}, age = {}".format(
            self.__class__.__name__,
            self.__name,
            self.__age
        )


b = B("Demo", 30)
print(b)

print(b.name) # property

# b.name = "Jack" # 不能改, error

b.age = 28 # setter
print(b)

print("-" * 50 + "\n")
