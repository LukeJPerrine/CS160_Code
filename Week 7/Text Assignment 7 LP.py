# Program that converts binary to decimal

# Input
binary = input('Provide binary number 8 integers long: ')

# Changes input to a list
blist = list(binary)

# Sets up list and counts for loop
barray = []
bcount = 8
ccount = 0

# Goes until the count = 8 (The number of integers in the input)
while ccount != 8:

        # Selects the last value from the list
        x = int(blist[-1])

        # Converts it to its binary equivalent
        y = (x * 2 ** (8 - bcount))

        # Adds converted integer to general list
        barray.append(y)

        # Adds counts, subtracts last integer to make sure it isn't repeated
        bcount = bcount - 1
        ccount = ccount + 1
        blist.pop()

# Sums the array/list to create the final decimal number
result = sum(barray)
print(result)