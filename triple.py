""" 
Take a function to use three times
Parameter
inner : function
    function to use func(*agrs) three times
"""
def tripler(func):
    def inner(*agrs):
        func(*agrs)
        func(*agrs)
        func(*agrs)
    return inner