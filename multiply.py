""" 
Python program to take in a list as input and multiply all of the 
elements in the list and return the result as output.
Parameter
    inputList: list[]
                the integer list as input
    result: int
                the result of multiplying all of the element
"""
def multiply_list(inputList):

    result = 1; 
    for i in range(0, len(inputList)):
        if int(i) == i:
            inputList[i] = int(inputList[i])
            result = result * inputList[i]
        else:
            return False
    return result

# driver code
inputList = []
inputList = [item for item in input("Input: ").split()]

print("Input: ", inputList)

print("Output: ", multiply_list(inputList))
