for i in range(10):
    print("hello world")

"""
i 浪費了，沒用到
"""

print("-" * 50 + "\n")
# -----------------------

for _ in range(10):
    print("hello world")
print(_) # 臨時變數

print("-" * 50 + "\n")
# -----------------------

x, y, *_ = [1, 2, 3, 4, 5]
print(x, y, _)

print("-" * 50 + "\n")
