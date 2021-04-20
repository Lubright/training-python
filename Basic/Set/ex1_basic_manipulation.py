# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 01:36:16 2021

@author: Lubright
"""

# initalize
a_set = set()
b_set = {1, 2, 3, 4, 5}
c_set = set(range(1,11))

print("{} ; type: {}".format(a_set, type(a_set)))
print("{} ; type: {}".format(b_set, type(b_set)))
print("{} ; type: {}".format(c_set, type(c_set)))
print("-" * 50 + "\n")

# add
a_set.add("Amy")
a_set.add("Benny")
a_set.add("Candy")
a_set.add("Amy")

print(a_set)
print("-" * 50 + "\n")

# remove
a_set.remove("Amy")
print(a_set)
print("-" * 50 + "\n")

# union
b_set = {1, 2, 3, 4, 5}
c_set = set(range(1,11))
setUnion = b_set | c_set
print(setUnion)
print("-" * 50 + "\n")

# intersection
b_set = {1, 2, 3, 4, 5}
c_set = set(range(1,11))

setIntersection = b_set & c_set
print(setIntersection)
print("-" * 50 + "\n")

# conversion
a_set = {"Amy", "Benny", "Candy", "Jack", "Iris"}
print(a_set)

a_list = list(a_set)
print(a_list)

b_set = set(a_list)
print(b_set)
print("-" * 50 + "\n")


