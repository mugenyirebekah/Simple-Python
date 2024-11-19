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

sentence = input("Enter a sentence: ")

words = sentence.split()
print(words)

####
