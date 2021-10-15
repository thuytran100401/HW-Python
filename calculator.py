"""
Calculate the number with the operator
Parameter
number1: float
	First number to calculate
number2: float
	second number to calculate
operator: str
	the operation
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
            return ValueError('invalid input')
        return number1 / number2
    elif operator == '//':
        if number2 == 0:
            return ValueError('invalid input')
        return number1 // number2
    elif operator == '-':
        return number1 - number2
    elif operator == '%':
        return number1 % number2
    else:
        return 'invalid input'

"""
Take the input to calculator and print out the input
"""
def parse_input():
    user_input = input("Enter equation: ")
    user_input = user_input.strip().split(" ")

    number1 = float(user_input[0])
    number2 = float(user_input[2])
    operator = user_input[1]


    print(calculator(number1, number2, operator))
