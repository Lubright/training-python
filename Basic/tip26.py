dict1 = {
    "a": 1,
    "b": 2
}

dict2 = dict() # 建立空 dict
print(dict2, type(dict2))
print("-" * 50 + "\n")

dict3 = dict(ab=1, cd=2) # 使用 **kwargs 去建立 dict
print(dict3)
print("-" * 50 + "\n")

list1 = [ ["a", 1], ["b", 2], ("c", 3) ]
dict4 = dict(list1) # 使用 iterable 去生成 dict
print(dict4)
print("-" * 50 + "\n")

x_list = [1, 2, 3, 4]
y_list = ["a", "b", "c", "d"]
dict5 = dict(zip(x_list, y_list))
print(dict5)
print("-" * 50 + "\n")

for item in zip(x_list, y_list):
    print(item) # tuple

print("-" * 50 + "\n")
