def func1(*args, **kwargs):
    print(args)
    print(kwargs)


func1("a", "b", "c", x=1, y=2)

print("-" * 50 + "\n")


def func2(x, y):
    return x + y

print(func2(**{"x": 1, "y": 2}))

