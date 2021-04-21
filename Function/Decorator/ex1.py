# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 01:36:16 2021

@author: Lubright
"""

import time

def calculate_execution_time(func): # decorator function
    def wrapper(*args, **kwargs):
        # t1 = time.time()
        # t1 = time.perf_counter() # 較精確
        t1 = time.perf_counter_ns() # 較精確
        # t1 = time.process_time() # 不包含sleep時間，只計算cpu運算時間
        # print(t1)
        result = func(*args, **kwargs)
        # t2 = time.time()
        # t2 = time.perf_counter()
        t2 = time.perf_counter_ns()
        # t2 = time.process_time()
        # print(t2)

        print("Time elapsed was", (t2 - t1), "ns")
        return result
    return wrapper

def sum1(n):
    result = 0
    for i in range(1, n+1):
        result += i
    return result

print(sum1(10))
sum1 = calculate_execution_time(sum1)
print( sum1(10) )
print("-" * 50 + "\n")

# use decorator
@calculate_execution_time
def sum2(n):
    result = 0
    for i in range(1, n+1):
        result += i
    return result

print( sum2(10) )
print("-" * 50 + "\n")

