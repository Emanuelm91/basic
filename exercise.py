#1 uneven numbers from 1-N while loop
maximum = int(input(" Please Enter the Maximum Value : "))

number = 1

while number <= maximum:
    if(number % 2 != 0):
        print("{0}".format(number))
    number = number + 1

#2 uneven numbers from 1-N for loop
maximum = int(input(" Please Enter any Maximum Value : "))

for number in range(1, maximum + 1):
    if(number % 2 != 0):
        print("{0}".format(number))

#3 Number squared
num = int (input ("please enter a number"))
print (num**2)

#4 Age of given person + 20 years
age = int(input("how old are you"))
print ('you will be in 20 years')
print (age + 20, )

# 5 price of product + 17%
Full_price = int(input ("show me the price +17% "))
print (Full_price * 1.17)

# 6 Plus , Divide , addition , Multilpication
num1 = int(input ("Please Enter a number"))
num2 = int(input("please enter another number"))
print (num1 + num2 , num1-num2 , num1 * num2 , num1/num2 )

# 7 Welcome + Date
import datetime
now = datetime.datetime.now()
x = input("welcome")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

#8 Avg of 4 given numbers
num1 = int (input("please enter first number "))
num2 = int (input("please enter second number "))
num3 = int (input("pl)ease enter third number "))
num4 = int (input("please enter fourth number "))
avg = (num4+num2+num3+num1)/4
print (avg)

#9 km\h
s=int(input('total speed:'))
d=int(input('total distance:'))
print(f'{s/d} time')

