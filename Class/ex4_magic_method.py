# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 01:36:16 2021

@author: Lubright
"""

class Point:
    hash_prime_1 = 1200556037
    hash_prime_2 = 2444555677

    def __init__(self, x: float = 0, y: float = 0) -> None:
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        return "{}, {}".format(self.x, self.y)
    
    def __repr__(self) -> str:
        return "Point({}, {})".format(self.x, self.y)
    
    def __hash__(self) -> int:
        n = self.x * Point.hash_prime_1
        return (n + self.y) % Point.hash_prime_2
    
    def __bool__(self):
        return (self.x and self.y)

    # 支援物件比較方法
    def __eq__(self, other: object) -> bool:
        """Implementation of ==; provides != for free.
        """
        return (self.x == other.x) and (self.y == other.y)
    
    def __lt__(self, other):
        """Implementation of <; provides > for free.
        """
        return ((self.x ** 2) + (self.y ** 2)) < ((other.x ** 2) + (other.y ** 2))
    
    def __le__(self, other):
        """Implementation of <=; provides >= for free.
        """
        return ((self.x ** 2) + (self.y ** 2)) <= ((other.x ** 2) + (other.y ** 2))

pt1 = Point(3, 4)
print(pt1) # call __str__()
print(pt1.__repr__())

print("-" * 50 + "\n")

pt2 = Point(6, 8)
print(pt1 > pt2)
print(pt1 <= pt2)
print("-" * 50 + "\n")


