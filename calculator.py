"""
Calculate the number with the operator
Parameter
number1: float
	First number to calculate
number2: float
	Second number to calculate
operator: str
	The operation
Return
	The number after calculate with the operation
"""
def calculator(number1, number2, operator):
    if operator == '*':
        return number1 * number2
    elif operator == '+':
        return number1 + number2
    elif operator == '**':
        return number1 ** number2
    elif operator == '/':
        if number2 == 0:
            return False
        return number1 / number2
    elif operator == '//':
        if number2 == 0:
            return False
        return number1 // number2
    elif operator == '-':
        return number1 - number2
    else:
        return False
"""
Take the input to calculator and print out the output
Parameter
UserInput: string
    equation enters by the user
number1: float
	First number to calculate
number2: float
	Second number to calculate
operator: str
	The operation
"""
def parse_input():
    try: 
        userInput = input("Enter equation: ")
        userInput = userInput.strip().split(" ")

        number1 = float(userInput[0])
        number2 = float(userInput[2])
        operator = userInput[1]
        print(calculator(number1,number2,operator))

    except ValueError:
        print(False)

