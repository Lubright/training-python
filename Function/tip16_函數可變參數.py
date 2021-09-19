def sum1(x, y):
    return x + y

print(sum1(1, 2))

print("-" * 50 + "\n")

def sum2(*args):
    return sum(args)

print(sum2(1, 2, 3, 4, 5))

print("-" * 50 + "\n")
