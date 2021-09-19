list1 = list("abcde") # using list()
print("list1:", list1, "; type:", type(list1))
print("-" * 50 + "\n")

list1 = [] # initial
list1.append("a")
list1.append("b")
list1.append("c")
list1.append("d")
list1.append("e")
print("list1:", list1, "; type:", type(list1))
print("-" * 50 + "\n")

list1 = list(range(1, 11)) # range
print("list1:", list1, "; type:", type(list1))
print("-" * 50 + "\n")

# iterate 1
for e in list1:
    print(e, sep=" ", end=", ")
print()
print("-" * 50 + "\n")

# iterate 2
for i in range(len(list1)):
    print(list1[i], sep=" ", end=", ")
print()
print("-" * 50 + "\n")

# iterate range
for i in range(10, 0, -1):
    print(i, end=", ")
print()
print("-" * 50 + "\n")

for i, v in enumerate(list1):
    print("{}:{}".format(i, v))

