"""
# 示範何謂有無副作用的函式
"""

# 沒有副作用
def subtract(number1, number2):
    return number1 - number2
print(subtract(123, 987))
print("-" * 50 + "\n")

# 有副作用
TOTAL = 0
def addTotal(amount):
    global TOTAL
    TOTAL += amount
    return TOTAL

print(addTotal(10))
print(addTotal(10))
print(TOTAL)
