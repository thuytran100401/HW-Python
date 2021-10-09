""" 
Python program to take in a list as input and multiply all of the 
elements in the list and return the result as output.
"""
def multiply_list(inputList):
    """ 
    The function multiply_list() will multiply all of the elements 
        in the list and return the result.
    """
    result = 1
    for number in inputList:
        result = result * number
    return result

# driver code
inputList = [int(item) for item in input("Input: "). split()]
print("Output: ", multiply_list(inputList))
