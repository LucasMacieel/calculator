def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

while True:
    
    print('1.Add')
    print('2.Subtract')
    print('3.Multiply')
    print('4.Divide')

    num = int(input('Enter the first number: '))

    operation = input('Enter the operation (1/2/3/4): ')

    num2 = int(input('Enter the second number: '))

    if operation in ('1', '2', '3', '4'):

        if operation == '1':
            print(f'The result is: {add(num, num2)}')
        elif operation == '2':
            print(f'The result is: {subtract(num, num2)}')
        elif operation == '3':
            print(f'The result is: {multiply(num, num2)}')
        elif operation == '4':
            print(f'The result is: {divide(num, num2)}')
    else:
        print('Invalid input')