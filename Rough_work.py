
'''Assignment = [44, 76, 22, 91]

Cs1 = ((Assignment[0]+Assignment[1]+Assignment[2]+Assignment[3])/4)

Cs2 = (Cs1/2)

print("Your coursework marks are", Cs2)

if(Cs2<35):
    print("Coursework marks are below 35.\n You CANNOT sit the exam.")

else:
    print("Permitted to sit exams")
'''

############################################################################
'''
total = 0

for i in range(1,3):
    total += i

print(f"sum of numbers from 1 to 13 is {total}")'''

#############################################################################
'''
def calc_yaka():
    amount_paid = 5000
    units = amount_paid/560
    print(f"You have {units:.2f} units of electricity")


def calc_water():
    units_consumed = 300
    amount_due = units_consumed*4100
    print(f"You owe {amount_due} for water")


def main():
    calc_yaka()
    calc_water()

main()
'''
#--------------------------------OR--------------------------#


'''def calc_yaka():
    amount_paid = 8000
    units = amount_paid/560
    return units

def calc_water():
    units_consumed = 990
    units_cost = units_consumed*4100
    return units_cost


def main():
    print(f"You have {units} yaka units")
    print(f"You owe {units_cost} for water.")'''


####################################################

#Question 1: Write a Python program that takes a list of integers as input and returns a list of even numbers.

'''
num = []

for i in range(1,11):
    value = eval(input(f"Enter a number {1}: "))
    num.append(value)


for i in num:
    if(i%2==0):
        print(i)

'''


#######################################################

#Question 2: Write a Python program to print the multiplication table of a given number up to 12.

'''num = eval(input("number to create a multiplication table with"))

for i in range(1,13):
    print(f"{num} x {i}  = {num*i}")'''

####################################################


'''
for i in range(1,6):
    for j in range(1,6):
        product = i * j
        print(f"{i} x {j} = {product}", end="\t")
    print()'''

####################################################

#Question 3: Write a Python program that finds the largest number in a list  USING the max() function.

'''num = [3,4234,3456, 345, 4535, 987]

largest_num = max(num)

print(f"The largest num is {largest_num}")'''


#Question 43 Write a Python program that finds the largest number in a list NOT USING the max() function.

'''num = [3, 45, 32, 23, 12, 1234]

largest = num[0]

for i in num:
    if (i > largest):
        largest = i

print(largest)'''


#Question 4: Write a Python function that checks if a string is the same as the input String

'''password = "Iron man"

ui = input("Enter the password: ")

if password == ui:
    print("Yooooo")

else:
    print("YIKES!!")'''


#################################
'''paragraph = "This is a \
 multi-line \
string \
Printed on the \
same line."


paragraph2 = """YOOOOOOOO.....
this is a multiline string...
            using

delimi t e r     s"""

print(paragraph)
print(paragraph2)

'''

###########

''''
def get_fname():
    fname = input("What's your first name? ")
    return fname

def get_lname():
    lname = input("...and last name? ")
    return lname

def main():
    fname = get_fname()
    lname = get_lname()

    print(fname)
    print("Your name is", fname, lname)
main()'''

#######################################
'''
response = input("What should I shout?")
shout = response.upper()

print(shout)'''

#####################################
'''
password = input("Tell me your password: ")
first_letter = password[0]
print(first_letter.upper())'''

#####################################
'''
num = input("Enter a number to be doubled: ")
dnum = float(num) * 2
print(dnum)
'''
#####################################
'''
num_pancakes = 10

print("I am going to eat " + str(num_pancakes) + " pancakes")
'''
############################

'''total_pancakes = 20

eaten_pancakes = 14

print("There are only " + str(total_pancakes - eaten_pancakes) + " pancakes left.")'''

########################################
'''
phrase = "I'm never going to dance again, guilty feet have got no rhythm"

print(phrase.find("dance"))

'''

########################

'''
print("Hello World!")
'''

########################
'''
name = input("Please enter your name: ")

print(name.upper())

'''

#########################


'''
number = eval(input("Enter a number:"))

if number % 2 == 0:
    print("even")

else:
    print("odd")

'''

#######################
'''
num = eval(input("Input number to compute factorial:"))

fact = 1
for i in range(1, num+1):
    fact = fact*i

print(fact)

'''
######################
'''
print(f"{3+5}, {7-2}, {8*3}, {10/2}")
'''
####################

'''
def greet():
    name = input("What is your name?: ")

    print("Hello, ", name)

greet()
'''
####################
'''
fname = "Rebekah"
lname = "Mugenyi"

name = (fname + " " + lname)

print(name)
'''
#####################
'''
str = input("Enter String: ")

print(len(str))
'''
#####################
'''
def num():

    num = eval(input("Enter a number: "))

    if num  == 0:
        print("zero")

    elif num < 0:
        print("negative")

    elif num > 0:
        print("positive")

num()

'''
######################
'''
C =eval(input("temp in C: "))

F = (9/5)*C+32

print(F)
'''
####################

'''
for i in range(10):
    print (i+1)
    
'''

###############
'''
num = eval(input("Multiplaction table number: "))

for i in range(1,13):
    print(f"{i} x {num} = {num*i}" )
'''
################

'''print("Becky".upper())'''
#################
'''
numbers = [1,2,3,4,5]

total = sum(numbers)
print(total)'''

#########
'''
sentence = input("Enter a sentence: ")

words = sentence.split()
print(words)
'''
####
'''
def create_list():
    num_list = []

    while True:
        data = eval(input("Enter an integer (type 0 when complete): "))

        if data == 0:
            break
        else:
            num_list.append(data)
        
    return num_list

def print_even_numbers(num_list):

    for i in num_list:
        if (i%2 ==0):
            print(i, end = " ")


def main():
    num_list = create_list()
    print_even_numbers(num_list)

main()
'''
#####################


#Write a Python program that takes a list of integers as input and returns a list of even numbers.
'''
def menu():
    print("This program takes a list of integers as input and returns a list of even numbers.")
    print('-'*80)
    print()

def integer_input():
    nums = []
    xStr = input("Please enter an integer to add to the list (Click enter when complete): ")

    while xStr != "":
        try:
            nums.append(int(xStr))
            xStr = input("Please enter an integer to add to the list (Click enter when complete): ")

        except ValueError:
            print("Error, please enter an integer")

    print("Input complete.")
    print(nums)

    return nums


def print_even(nums):

    for i in nums:
        if i%2 == 0:
            print(i)


def main():
    menu()
    nums = integer_input()
    print_even(nums)

main()

'''
##############################################################################################

'''
import math

a, b, c = eval(input("Enter coefficients:"))

d = b*b-4*a*c

if d < 0:
    print("Try different values")

else:

    d1 = math.sqrt(d)
    x1 = (-b - d1 )/(2*a)
    x2 = (-b + d1)/(2*a)

    print(x1)
    print()
    print(x2)


'''
##############################################################################################
'''
from graphics import *

win = GraphWin("Celsius Temperature", 300,200)
win.setCoords(0.0,0.0,3.0,4.0)

Text(Point(1,3), 'Celsius Temperature: ').draw(win)
Text(Point(1,1), 'Fahrenheit Temperature: ').draw(win)

input_txt = Entry(Point(2,3),5)
input_txt.setText('0.0')
input_txt.draw(win)

output = Text(Point(2,1), "")
output.draw(win)

button = Text(Point(1.5,2), "Convert It")
button.draw(win)

Rectangle(Point(1.5,1.5), Point(2,2))

win.getMouse()

c = input_txt.getText()

f = 9/5 * eval(c) + 32

output.setText(f)

button.setText("Quit")

win.getMouse()

'''
#######################################################################################
'''
# average1.py
#    A program to average a set of numbers
#    Illustrates counted loop with accumulator


def main():
    n = eval(input("Enter the number of entries: "))

    sum = 0
    
    for i in range(n):
        x = eval(input("Number: "))
        sum = sum + x

    print(sum/n)
main()
'''

##################################################################################
'''
def main():
    moredata = 'yes'

    sum = 0
    count = 0

    while moredata == 'yes':
        x = eval(input("Enter number: "))
        sum = sum + x
        count = count + 1

        moredata = input("Moredata? ")
    
    print(sum/count)
        

main()
'''
##################################################################
'''

def main():
    sum = 0
    count = 0

    x = eval(input("Please enter the a number (negative to quit): "))

    while x > 0:
        sum = sum+x
        count = count+1    
        x = eval(input("Please enter the a number (negative to quit): "))

    print(sum/count)    

main()
'''
#####################################################################
'''

def main():

    sum = 0
    count = 0

    xStr = input("Enter the number: ")

    while xStr != "":
        sum = sum + int(xStr)
        count = count + 1
        
        xStr = input("Enter the number: ")

    print(sum/count)

main()
'''
#####################################################################

'''
def main():

    filename = input("What is the file name?")
    inFile = open(filename, 'r')

    sum = 0
    count = 0

    for i in inFile.readlines():
        sum = sum + eval(i)
        count = count + 1

    print(sum/count)


main()
'''
#####################################################################
'''
def main():

    filename = input("What is the filename? ")
    infile = open(filename, 'r')

    sum = 0
    count = 0

    line = infile.readline()

    while line != "":
        sum = sum + eval(line)
        count = count + 1
        line = infile.readline()

    print(sum/count)

main()
'''
###############################################################
'''

import string

def main():
    fileName = input("What file are the numbers in?")
    infile = open(fileName, 'r')

    sum = 0
    count = 0

    line = infile.readline()

    while line != "":
        for xStr in line.split(','):
            sum = sum + eval(xStr)
            count = count+1

            
        line = infile.readline()

    print(sum/count)

main()
'''
################################################################
'''
while True:
    x = eval(input("Enter a positive number: "))
    if x >= 0: 
        break
    else:
        print("The number you entered was not positive")

'''
#############################################################

'''

while True:
    x = eval(input("Enter a positive number: "))
    if x >=0: break
    print("The number you entered was not positive.")

'''
####################################################
'''
ans = input("What car would you like?")

if ans:
    car = ans
else:
    car = "volvo"

print(car)
'''
###################################
'''
ans = input("What car would you like?")
car = ans or "Benz"
print(car)
'''
##################################
'''
car = input("What car do you want?") or "Benz"
print(car)
'''
###################################
'''
def menu():
    print("This program checks to see if two strings are the same")
    print('-'*80)

def check_string():
    string = 'Password'
    input_string = input('Enter a string: ')

    if string == input_string:
        print("The strings are the same")

    else:
        print("The strings are different")


def main():
    menu()
    check_string()

main()

'''
###################################
'''
def main():
    print('This program prints a multiplication table')
    print('-'*70)
    #n = eval(input('Enter a number to print the multiplication table.'))

    for j in range(1,13):
        for i in range(1,13):
            print(f"{i:<2} x {j:<2} = {i*j:<5}", end = " ")
        print()

main()
'''
##################################
'''
def menu():
    print("This program prints the even numbers in a list")
    print('-'*60)

def create_list():
    num_list = []

    xStr = input("Enter a number to include in the list (Enter when complete)")

    while xStr != '':
        x = eval(xStr)
        num_list.append(x)
        xStr = input("Enter a number to include in the list (Enter when complete)")

    print("List complete", num_list)
    
    return num_list

def get_even_numbers(num_list):
    for i in num_list:
        if i % 2 == 0:
            print(i)

def main():
    menu()
    num_list = create_list()
    get_even_numbers(num_list)

main()
'''
################################
'''
nlist = [3,2,5,1,234,5153, 2,3]

largest = nlist[0]

for i in nlist:
    if i > largest:
        largest = i

print(largest)
'''
#################################
'''
s1 = "Animals"
s2 = "Badger"
s3 = "Honey Bee"
s4 = "Honey Badger"

print()

print(s1.lower())
print()
print(s2.lower())
print()
print(s3.lower())
print()
print(s4.lower())

print()
'''
###################################
'''

s1 = "Animals"
s2 = "Badger"
s3 = "Honey Bee"
s4 = "Honey Badger"

print()

print(s1.upper())
print()
print(s2.upper())
print()
print(s3.upper())
print()
print(s4.upper())

print()
'''
#################################
'''
from graphics import *

win = GraphWin("Yoski")


center = Point(100,100)

circ = Circle(center, 30) 

circ.draw(win)
circ.setFill("red")

rec = Rectangle(Point(10,10),Point(90,90))
rec.draw(win)

rec.setFill("Yellow")

l = Line(Point(70,70), Point(90,90))
l.draw(win)

o = Oval(Point(40,50), Point(190,80))
o.draw(win)

txt = Text(center, 'YAAAAY')
txt.draw(win)

win.getMouse()
'''
###################################

'''
def main():
    n = eval(input("Enter the number to create factorial of: "))

    fact = 1

    for i in range(n,1,-1):
        fact = fact * i

    print(fact)

main()
'''
#############################
