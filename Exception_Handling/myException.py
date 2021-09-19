# 定義自己的excpetion

class MyException(Exception):
    pass

class NameTooShort(MyException):
    pass

class NameTooLong(MyException):
    pass

class NameNotFound(MyException):
    pass