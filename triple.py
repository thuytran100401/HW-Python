""" 
Take a function to use on three times
Parameter
inner : function
    function to use func(*agrs) on three times
"""
def tripler(func):
    def inner(*agrs):
        func(*agrs)
        func(*agrs)
        func(*agrs)
    return inner