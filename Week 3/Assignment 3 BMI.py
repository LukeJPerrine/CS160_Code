#Calculator for BMI (Body Mass Index)

#BMI = (weight(lbs)*703)/(height(in)*height(in))

feet = input('Please enter your height in feet: ')

inches = input('and inches: ')

weight = input('Please enter your weight in pounds: ')

feet = int(feet)
inches = int(inches)
weight = int(weight)

height = (feet * 12) + inches

height = int(height)

print(height)

BMI = (weight * 703) / (height * height)

print('Your BMI is ', BMI)
