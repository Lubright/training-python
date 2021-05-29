false_values = [
    False,
    [],
    {},
    '',
    0,
    0.0,
    None
]

for value in false_values:
    # print('{} is {}'.format(value, bool(value)))
    print(True if value else False)

print("-" * 50 + "\n")


# 自定義類別的 True 和 False
class MyType:
    def __init__(self) -> None:
        self.value = []
    
    def add(self, x):
        self.value.append(x)
    
    def __bool__(self):
        return bool(self.value)

my_type = MyType()
print('{} is {}'.format(my_type, bool(my_type)))

my_type.add(1)
print('{} is {}'.format(my_type, bool(my_type)))

print("-" * 50 + "\n")

a = []

if a == []:
    print("a is empty")

if not a: # 檢測 a 是否 empty, 推薦
    print("a is empty")
