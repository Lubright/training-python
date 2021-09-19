def validate(name):
    if len(name) < 10:
        raise ValueError("len of name less than 10")

try:
    validate("test")
except ValueError as e:
    print(e)

# 定義自己的excpetion

from myException import NameTooShort

def validate2(name):
    if len(name) < 10:
        raise NameTooShort("name is too short")


try:
    validate2("test")
except Exception as e:
    print(e)