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
        if inputList[i].isdigit():
            inputList[i] = int(inputList[i])
            result = result * inputList[i]
        else:
            return False
    return result

# driver code
inputList = []
input = input("Input: ").split(" ")
inputList = [item for item in input]

print("Input: ", inputList)

print("Output: ", multiply_list(inputList))
