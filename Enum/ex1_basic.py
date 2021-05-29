from enum import Enum

Month = Enum("Month", ('Jan', 'Feb', 'Mar'))

print(Month, type(Month))
print("-" * 50 + "\n")

temp = Month.Jan

print(temp, type(temp))
print(temp.name, temp.value)
print(dir(temp))

print("-" * 50 + "\n")

temp2 = Month.Jan

print(temp == temp2)
print(temp is temp2)

print("-" * 50 + "\n")

class MyMonth(Enum):
    Jan = 1 # class static member
    Feb = 2
    Mar = 3

    @classmethod
    def getDefaultMonth(cls):
        return cls.Jan

temp = MyMonth.Jan

print(temp, type(temp))
print(temp.name, temp.value)

print("-" * 50 + "\n")


temp = MyMonth(1)
temp2= MyMonth.Jan

print(temp, type(temp))
print(temp == temp2)
print(temp is temp2)

print("-" * 50 + "\n")

# iteration the enum class

print(list(MyMonth))

print("-" * 50 + "\n")

print(MyMonth.getDefaultMonth())
