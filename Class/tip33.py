class Person:
    def __init__(self, name, age) -> None:
        self.__name = name
        self.__age = age
    
    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age
    
    @name.setter
    def name(self, name):
        self.__name = name

    @age.setter
    def age(self, age):
        self.__age = age
    
    def __str__(self) -> str:
        return "[{}] name = {}, age = {}".format(
            self.__class__.__name__,
            self.name,
            self.age
        )
    
    # 比較優先
    def __repr__(self) -> str:
        return "[{}] name = {}, age = {}".format(
            self.__class__.__name__,
            self.name,
            self.age
        )
    
    
p1 = Person("Amy", 23)
print(p1)