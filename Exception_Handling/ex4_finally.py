def divide(x, y):
    try:
        ans = x / y
    except Exception as e:
        print(e)
    else:
        return ans
    finally:
        print("一定執行")
        

# test here
print("2/3={}".format(divide(2, 3)))
print("a/b={}".format(divide("a", "b")))
print("2/0={}".format(divide(2, 0))) # 捕捉到 ZeroDivisionError
print("-" * 50 + "\n")