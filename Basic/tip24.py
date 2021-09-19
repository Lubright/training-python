# Tuple 的創建

tuple1 = (1, 2, 3, "Python", 5, 6)
print(tuple1)
print("-" * 50 + "\n")


tuple2 = 1, 2, 3
print(tuple2, type(tuple2))
print("-" * 50 + "\n")

tuple3 = 1,
print(tuple3, type(tuple3))
print("-" * 50 + "\n")

# 解構
x, y, z = tuple2
print(x, y, z)
print("-" * 50 + "\n")

# 解構2
x, y, *_ = tuple1

print(x, y, _)
print("-" * 50 + "\n")

list1 = [1, 2, 3, 4]
for i, v in enumerate(list1):
    print("{}: {}".format(i, v))

for item in enumerate(list1):
    print(item) # tuple

print("-" * 50 + "\n")

# swap
x = 1; y = 2
print(x, y)

x, y = y, x
print(x, y)
print("-" * 50 + "\n")
