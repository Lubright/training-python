import os
import sys

d1 = {
    'name': 'Python',
    'age': 27
}

d2 = {
    'version': 3.6,
    'platform': sys.platform
}

d3 = {
    'size': '59MB'
}

print(d1)
print(d2)
print(d3)

print("-" * 50 + "\n")


a = {}

for k, v in d1.items():
    a[k] = v
for k, v in d2.items():
    a[k] = v
for k, v in d3.items():
    a[k] = v

print(a)

print("-" * 50 + "\n")


# 比較好的做法

a = {}
d1.update(d2)
d1.update(d3)
print(d1)

print("-" * 50 + "\n")

# 比較好的做法
d1 = {
    'name': 'Python',
    'age': 27
}

d2 = {
    'version': 3.6,
    'platform': sys.platform
}

d3 = {
    'size': '59MB'
}

a = {**d1, **d2, **d3} # python3.5 以上

print(a)

print("-" * 50 + "\n")
