
def fib(n):
    """
    使用傳統的方式生成 list
    """
    numbers = []
    current, next_num = 0, 1 # inital seed
    while len(numbers) < n:
        current, next_num = next_num, current + next_num
        numbers.append(current)
    return numbers

a = fib(5)
print(a)
print("-" * 50 + "\n")
# ----------------------------

def fib_gen(n):
    """
    """
    cnt = 0
    current, next_num = 0, 1 # inital seed
    while cnt < n:
        current, next_num = next_num, current + next_num
        cnt += 1
        yield current

for e in fib_gen(5):
    print(e)

print("-" * 50 + "\n")
# ----------------------------

def fib_gen2():
    """
    無限生成器
    """
    current, next_num = 0, 1 # inital seed
    while True:
        current, next_num = next_num, current + next_num
        yield current

for e in fib_gen2():
    if e > 1000:
        print(e)
        break
    else:
        print(e, end=", ")

print("-" * 50 + "\n")
