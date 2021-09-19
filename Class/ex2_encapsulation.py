# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 01:36:16 2021

@author: Lubright
"""

class CCircle:
    PI = 3.14
    CNT = 0
    def __init__(self, name: str = "", r: float = 0.0) -> None:
        self.__name = name
        self.__r = r
        CCircle.__addCNT()
    
    # public instance method
    def area(self) -> float:
        return pow(self.__r, 2) * CCircle.PI
    
    # private instance method
    def __private_instance_method(self) -> None:
        print("__private_instance_method is called...")
    def call_private_instance_method(self) -> None:
        self.__private_instance_method()
    
    def __str__(self) -> str:
        return "[CCircle] name = {}, r = {}, area = {:.2f}".format(self.__name, self.__r, self.area())

    # public static method
    @staticmethod
    def getCNT() -> int:
        return CCircle.CNT

    # private static method
    @staticmethod
    def __addCNT() -> None:
        CCircle.CNT += 1

    # class method like factory pattern
    @classmethod
    def generateObject(cls, name, r):
        return cls(name, r)
    

c1 = CCircle(name="c1", r=2)
print(c1)
print(CCircle.CNT)
print(CCircle.getCNT())
c1.call_private_instance_method()
print("-" * 50 + "\n")

c2 = CCircle.generateObject("c2", 5)
print(c2)