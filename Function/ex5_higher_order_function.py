def callItTwice(func, *args, **kwargs):
    func(*args, **kwargs)
    func(*args, **kwargs)
callItTwice(print, "I love you!")