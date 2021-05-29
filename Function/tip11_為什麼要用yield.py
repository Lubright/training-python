a = range(100000)

print(a)

def my_range(n):
    result = 0
    while result<=n:
        yield result
        result += 2

print("-" * 50 + "\n")

b = my_range(100000)

print(b)
print(b.__next__())
print(b.__next__())

print("-" * 50 + "\n")
