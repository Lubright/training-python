dict1 = {
    'name': 'Python',
    'age': 27,
    'version': 3.6
}

# 好的方式
print(dict1.get('name', 'default'))
print(dict1.get('name2', 'default'))
print(dict1.get('name3')) # default: None

print("-" * 50 + "\n")


# 傳統方式
try:
    print(dict1)
    print(dict1["name"])
    print(dict1["name2"])
except Exception as e:
    print('error for key {}'.format(e))

print("-" * 50 + "\n")


from collections import defaultdict

dict2 = defaultdict(lambda: "missing", dict1) # default return value = "missing"

print(dict2)

print(dict2.get('name'))
print(dict2.get('name2')) # None
print(dict2["name2"]) # missing
