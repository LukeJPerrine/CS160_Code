# Text Assignment 8
# This code takes input integers and creates a list to output

xlist = []

while True:
    # Checks if input is a number or not
    while True:
        x = input("Please enter a number, or 0 to quit: ")
        try:
            x = int(x)
            break
        except ValueError:
            print("That is not a number, please try again.")

    # Checks if number is zero, breaks if true
    if x == 0:
        break

    # Adds to list
    else:
        xlist.append(x)

# Sums up list
final = sum(int(i) for i in xlist)

print("The sum of your entered values is: ", final)

