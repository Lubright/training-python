import lib.myMath

def main():
    print("Hello Python")
    print("PI:", lib.myMath.PI)
    print("fact(5):", lib.myMath.fact(5))

if __name__ == "__main__":
    print("{} as main program".format(__name__))
    # test __file__
    main()
    print("-" * 50 + "\n")
