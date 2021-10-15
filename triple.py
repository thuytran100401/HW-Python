def tripler(func):
    def inner(*agrs):
        func(*agrs)
        func(*agrs)
        func(*agrs)
    return inner