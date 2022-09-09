print('multiplication calculator')
print('*************************')
number1 = int(input('1: '))
number2 = int(input('2: '))
print('*************************')


def multiply(number1,number2):
    return number1 * number2

calc = multiply(number1,number2)

print(f'the answer is: {calc}')