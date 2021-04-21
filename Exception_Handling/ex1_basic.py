
# ZeroDivisionError
def divide(x, y):
    try:
        ans = x / y
    except ZeroDivisionError as e:
        print(e)
    except TypeError as e:
        print(e)
    else: # 如果程式執行正確，則執行此區塊的程式
        return ans

print("2/3={}".format(divide(2, 3)))
print("2/0={}".format(divide(2, 0))) # 捕捉到 ZeroDivisionError
# print("a/b={}".format(divide("a", "b"))) # 拋出的 error 物件沒有捕捉到程式終止
print("-" * 50 + "\n")


# FileNotFoundError
try:
    with open("xyz.txt", mode="rt", encoding="utf-8") as fin:
        data = fin.read()
except FileNotFoundError as e:
    print(e)
else:
    print(data)
print("-" * 50 + "\n")

# 使用一個 except 捕捉多個異常
def divide(x, y):
    try:
        ans = x / y
    except (ZeroDivisionError, TypeError):
        print("除數為0或使用字元做除法運算異常")
    else:
        return ans

print("2/3={}".format(divide(2, 3)))
print("a/b={}".format(divide("a", "b")))
print("-" * 50 + "\n")


# 通用 Exception 物件
def divide(x, y):
    try:
        ans = x / y
    except Exception as e:
        print(e)
    else:
        return ans

print("2/3={}".format(divide(2, 3)))
print("a/b={}".format(divide("a", "b")))
print("-" * 50 + "\n")