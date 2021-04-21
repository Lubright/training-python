from functools import reduce

PI = 3.14

def fact(n):
    result = 1
    result = reduce(lambda x, y: x*y, range(1, n+1), 1)

    return result

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

if __name__ == "__main__":
    print("{} as main program".format(__name__))
    # test myMath
    print(fact(5))
    print("-" * 50 + "\n")
else:
    print("{} as module".format(__name__))
    print("-" * 50 + "\n")