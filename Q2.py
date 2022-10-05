import math


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multibly(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def exponentiation(num1, num2):
    return num1 ** num2


def modulus(num1, num2):
    return num1 % num2


first_number = input('Enter 1st number: ')
while not first_number.isdigit():
    print("Invalid input! Please enter right number")
    first_number = input('Enter 1st number: ')
    if first_number.isdigit():
        continue
print(''' 1_ +
2_ -
3_ *
4_ /
5_ ^
6_ % ''')
operation = input('Select operation: ')
valid_operation = ('1', '+', '2', '-', '3', '*', '4', '/', '5', '^', '6', '%')
while operation not in valid_operation:
    print("Please enter valid operation")
    operation = input('Select operation: ')
    if operation in valid_operation:
        continue

second_number = input('Enter another number please: ')
while not second_number.isdigit():
    print("Invalid input! Please enter right number")
    second_number = input('Enter another number please: ')
    if second_number.isdigit():
        continue
result = 0

if operation == '1' or operation == '+':
    result = add(int(first_number), int(second_number))
    print(first_number, "+", second_number, "=", result)
elif operation == '2' or operation == '-':
    result = subtract(int(first_number), int(second_number))
    print(first_number, "-", second_number, "=", result)
elif operation == '3' or operation == '*':
    result = multibly(int(first_number), int(second_number))
    print(first_number, "*", second_number, "=", result)
elif operation == '4' or operation == '/':
    result = divide(int(first_number), int(second_number))
    print(first_number, "/", second_number, "=", result)
elif operation == '5' or operation == '^':
    result = exponentiation(int(first_number), int(second_number))
    print(first_number, "^", second_number, "=", result)
elif operation == '6' or operation == '%':
    result = modulus(int(first_number), int(second_number))
    print(first_number, "%", second_number, "=", result)
extra_calculation = input('''Would you like do more calculations on the output?
1_ Round.
2_ Floor.
3_ Ceiling.
4_ No, Thanks.
Your decision: ''')

if extra_calculation == 'Round' or extra_calculation == '1':
    print("Final result=", round(float(result)))
elif extra_calculation == 'Floor' or extra_calculation == '2':
    print("Final result=", math.floor(float(result)))
elif extra_calculation == 'Ceiling' or extra_calculation == '3':
    print("Final result=", math.ceil(float(result)))
elif extra_calculation == 'No, Thanks.' or extra_calculation == '4':
    pass
print("Thank you for using our program:)")
