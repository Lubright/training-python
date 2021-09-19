class A:
    """
    public var
    """
    def __init__(self, name, age) -> None:
        self.name = name
        self.__age = age
        # self.protect_var = 1
        self._protect_var = 1 # protect var, 提醒用戶是 protect var, 但用戶還是可以存取

    def __str__(self) -> str:
        return "My name is {}, I'm {} years old, protect value={}".format(
            self.name,
            self.__age,
            self._protect_var
        )

a = A(name="Python", age=27)
print(a)

a._protect_var = 2
print(a._protect_var)

# print(a.__age) # error, 因為是 private var
print(a._A__age) # 還是可以，但 dir 看不到

print("-" * 50 + "\n")

print(dir(a))



