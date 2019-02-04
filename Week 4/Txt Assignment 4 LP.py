# Text Assignment 4
# Calculator

print('Simple Calculator')

# Inputs
opin = input('Please input your operator (+, -, *, /): ')
i = input('Please enter the first number: ')
j = input('Please enter the second number: ')
i = int(i)
j = int(j)

# Multiplication
if opin == '*':
    out = (i * j)
    print('Result = ', out)

# Addition
elif opin == '+':
    out = (i + j)
    print('Result = ', out)

# Division
elif opin == '/':
    if j == 0:
        print('Cannot Divide by 0')
    else:
        out = (i / j)
        print('Result = ', out)

# Subtraction
elif opin == '-':
    out = (i - j)
    print('Result = ', out)

# Invalid op test
else:
    print('Invalid Operator')
