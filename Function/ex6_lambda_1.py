func1 = lambda x: print(x)
func1([1, 2, 3, 4])
print("-" * 50 + "\n")

func2 = lambda list1: (list1[0] * 2) + (list1[1] * 2)
print(func2([2, 5]))
print("-" * 50 + "\n")

import random

rects = []
for i in range(10):
    temp_list = [random.randint(1, 11), random.randint(1, 11)]
    rects.append(temp_list)
print("rects:", rects)
print("sorted by perimeter(ascending):", sorted(rects, key=lambda list1: (list1[0] * 2) + (list1[1] * 2), reverse=False))
print("sorted by perimeter(descending):", sorted(rects, key=lambda list1: (list1[0] * 2) + (list1[1] * 2), reverse=True))