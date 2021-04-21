from functools import reduce

sum1 = reduce(lambda x, y: x+y, range(1, 11))
print("sum1:", sum1)

sum2 = reduce(lambda x, y: x+y, range(1, 11), 1)
print("sum2:", sum2)