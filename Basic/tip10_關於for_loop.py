a = [1, 2, 3]

for e in a:
    print(e)

print("-" * 50 + "\n")

print(dir(a))

print("-" * 50 + "\n")

# iterable class
print("iterable class")

class A:
    def __init__(self) -> None:
        self.data = []
    
    def add(self, x):
        self.data.append(x)
    
    def __iter__(self):
        # return self.data.__iter__() # 方法一: 實現 iterable
        # 方法二: 使用 yield
        for e in self.data:
            yield e

class B:
    def __init__(self, **kwargs) -> None:
        # print(kwargs)
        self.x = kwargs["x"]
        self.y = kwargs["y"]
    
    def __str__(self):
        return f"[{self.__class__.__name__}] " \
            f"x = {self.x}, " \
            f"y = {self.y}"


b1 = B(x=1, y=2)
b2 = B(x=3, y=4)

a = A()
a.add(b1)
a.add(b2)

# implement __iter__ for loop
for e in a:
    print(e)

print("-" * 50 + "\n")


# yield_generator

print('yield_generator')
a = [1, 2, 3, 4]

def get_item():
    for e in a:
        yield e

b = get_item()
print(b) # generator object

print(dir(b)) # 有 __iter__()

for e in b:
    print(e)

print("-" * 50 + "\n")



