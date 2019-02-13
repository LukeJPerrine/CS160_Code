# Text Assignment 6, Odd and Even Sums

# Explanation
print('This program is designed to calculate the sum of even and odd numbers between two set numbers')

# Inputs
first = int(input('Please enter the first number of the range: '))
last = int(input('Please enter the last number of the range: '))

# Initial odd and even arrays
evenlist = []
oddlist = []

# Initial sums
sume = 0
sumo = 0

numbers = list(range(first, last+1))

for x in numbers:
    if x % 2 == 0:
        evenlist.append(x)
    else:
        oddlist.append(x)

print(evenlist)
print(oddlist)

sume = sum(int(i) for i in evenlist)
sumo = sum(int(j) for j in oddlist)

print('The even sum of this range is: ', sume)
print('The odd sum of this range is: ', sumo)