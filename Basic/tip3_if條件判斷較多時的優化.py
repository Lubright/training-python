import random
from enum import Enum
from types import CodeType

class Condition(Enum):
    A = 1
    B = 2
    C = 3
    D = 4

    @staticmethod
    def case1(): 
        print("case1...")
        values = [1, 2, 3, 4]
        choice = Condition(random.choice(values))
        print("chocie:", choice)

        if choice is Condition.D: # 比較好的方式
            print('go to step two')
        else: # 其他
            print('go to step one')

        print("-" * 50 + "\n")
    
    @staticmethod
    def case2():
        print("case2...")
        values = [1, 2, 3, 4]
        choice = Condition(random.choice(values))
        print("chocie:", choice)
        
        if choice == Condition.A or choice == Condition.B:
            print('go to step one')
        else:
            print('go to step two')

        print("-" * 50 + "\n")

    @staticmethod
    def case3():
        """嘗試用集合判斷，比較好的方式
        """
        print("case3...")
        values = [1, 2, 3, 4]
        choice = Condition(random.choice(values))
        print("chocie:", choice)

        options_set = set((Condition.A, Condition.B))
        print("options_set:", options_set)
        
        if choice in options_set:
            print('go to step one')
        else:
            print('go to step two')

        print("-" * 50 + "\n")

    @staticmethod
    def case4():
        """嘗試用 list 判斷，比較好的方式，效率最好
        """
        print("case4...")
        values = [1, 2, 3, 4]
        choice = Condition(random.choice(values))
        print("chocie:", choice)

        options_set = (Condition.A, Condition.B)
        print("options_set:", options_set)
        
        if choice in options_set:
            print('go to step one')
        else:
            print('go to step two')

        print("-" * 50 + "\n")


Condition.case1()

Condition.case2()

Condition.case3()

Condition.case4()

