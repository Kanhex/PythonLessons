def print_digit(symbol):
    print(symbol)


def addition(digit1, digit2):
    print(digit1 + digit2)


def subtraction(digit1, digit2):
    print(digit1 - digit2)


def division(digit1, digit2):
    print(digit1 / digit2)


def multiplication(param, param1):
    print(param * param1)


def calculate(digit1, digit2, symbol):
    if symbol == "+":
        addition(digit1, digit2)
    elif symbol == "-":
        subtraction(digit1, digit2)
    elif symbol == "/":
        division(digit1, digit2)
    elif symbol == "*":
        multiplication(digit1, digit2)
    else:
        print("Действие не потдерживается")




'''
print_digit("****")
print_digit("*  *")
print_digit("*  *")
print_digit("*  *")
print_digit("****")
'''
'''
addition(5, 2)
subtraction(5, 2)
division(5, 2)
multiplication(5, 2)
'''
calculate(1, 2, "*")


        









