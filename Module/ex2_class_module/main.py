from lib.bank import Bank, Shilin_Bank
# from lib.bank import *
import sys

print("sys.path:", sys.path)
print("-" * 50 + "\n")

account1 = Bank("James", 1000)
print("account1:", account1)
print("-" * 50 + "\n")

account2 = Shilin_Bank("Amy", 2000)
print("account2:", account2)
print("-" * 50 + "\n")

from lib.zhongzheng_bank import Zhongzheng_Bank

account3 = Zhongzheng_Bank("Candy", 2000)
print("account3:", account3)
print("-" * 50 + "\n")