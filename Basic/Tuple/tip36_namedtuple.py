from collections import namedtuple

Car = namedtuple("Car", "color mileage automatic")
car1 = Car("red", 3812.4, True)

print(car1)

car2 = Car("red", 3812.4, 0) # 比較沒有個別參數的 datatype

print("-" * 50 + "\n")

# 改善的 namedtuple
from typing import NamedTuple # python3.6 以上 support

class Car(NamedTuple):
    color: str
    mileage: int
    automatic: bool

car1 = Car("red", 1000.01, False)
print(car1, type(car1))


car1 = Car("red", 1000.01, 0) # 不會有 error, 除非使用 mypy to check
print(car1, type(car1))
