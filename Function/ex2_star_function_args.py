# 使用 * 建立可變參數函式
## function接收參數設計原則:
### 1. ex: sum() 只接受單一可迭代引數
### 2. ex: min, max function 除了可接收單一可迭代引數，還可以接收多個參數

# sum()
print(sum([1, 2, 3, 4]))
print("-" * 50 + "\n")

# max()
print(max(1, 2, 3, 4))
print(max([1, 2, 3, 4]))
print("-" * 50 + "\n")

# self-defined 可變參數 (varargs function)
def myProduct(*args):
    result = 1
    for e in args:
        result *= e
    return result
print(myProduct(1, 2, 3, 4))
print(myProduct(1, 2, 3, 4, 5))
print("-" * 50 + "\n")

# 除了可接收單一可迭代引數，還可以接收多個參數
def myMinFunction(*args):
    print("args:", args)
    print("type of args:", type(args)) # tuple

    if len(args) == 1:
        values = args[0] # 單個可迭代參數
    else:
        values = args # 多個輸入參數

    # no args input, raise error, or only one non iterable argument
    if len(values) == 0:
        raise ValueError("myMinFunction() args is an empty sequence")
    
    minIndex = 0
    minValue = values[0]
    for i, v in enumerate(values):
        if v < minValue:
            minValue = v
            minIndex = i
    return minIndex, minValue


minIndex, minValue = myMinFunction(1, 2, 3, 4)
print("minIndex = {}, minValue = {}".format(minIndex, minValue))
print("-" * 50 + "\n")

minIndex, minValue = myMinFunction([1, 2, 3, 4])
print("minIndex = {}, minValue = {}".format(minIndex, minValue))
print("-" * 50 + "\n")

# minIndex, minValue = myMinFunction(1) # meaningless
# print("minIndex = {}, minValue = {}".format(minIndex, minValue))
# print("-" * 50 + "\n")

minIndex, minValue = myMinFunction([1])
print("minIndex = {}, minValue = {}".format(minIndex, minValue))
print("-" * 50 + "\n")
