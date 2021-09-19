## 簡單的話，使用 dict or tuple

### 1.1 dict: 數據可以任意修改，但沒有順序

### 1.2 tuple: 不能改變，但有順序


## 如果想給數據增加一些自定義的行為方法，請使用 class

### 2.1 普通的 class

### 2.2 NamedTuple
from typing import NamedTuple

class Car(NamedTuple):
    color: str
    mileage: float
    automatic: bool

    def __repr__(self) -> str:
        return f"[{self.__class__.__name__}]: color = {self.color}; mileage = {self.mileage}; automatic = {self.automatic}"

    def run(self):
        pass


car1 = Car("green", 3812.4, True)

print(car1)