# 用函式表模擬 switch
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

# 使用 list
fn = [add, subtract, multiply, divide]

result = fn[0](1, 2)
print("result = {}".format(result))
print("-" * 50 + "\n")


# 使用 dict
fn_dict = {"add": add, "subtract": subtract, "multiply": multiply, "divide": divide}

result = fn_dict["multiply"](2, 8)
print("result = {}".format(result))
print("-" * 50 + "\n")
