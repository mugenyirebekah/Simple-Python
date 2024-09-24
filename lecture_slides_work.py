
###PPT 1 Page 33:

#File: chaos.py
#A simple program illustrating chaotic behavior

'''def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range (10):
        x = 3.9 * x * (1 - x)
        print(x)
main()'''

###PPT 2 Page 10:



#my attempt
# 

'''def main():
    input_temp = float(input("Enter the temperature in Celsius: "))
    output_temp = (input_temp*9/5) + 32

    print("The temperature in Fahrenheit is", output_temp)


main()'''

#from the slide


# A program to convert Celsius temps to Fahrenheit 
# by: Susan Computewell

'''def main():

    celsius = eval(input("What is the Celsius temperature? ")) 
    fahrenheit = (9/5) * celsius + 32
    print("The temperature is ",fahrenheit," degrees Fahrenheit.")
main()'''

'''print(3+4)

print("the answer is", 3+4)'''

'''x = 3
y = 4
print(x,y)
x, y = y, x 
print(x,y)'''

'''def spamneggs():
    spam, eggs = eval(input("Enter # of slices of spam followed by # of eggs: ")) #use commas to separate input
    print("You ordered", eggs, "eggs and", spam, "slices of spam. Yum!")

spamneggs()'''




'''for i in [0,1,2,3]:
    print (i)'''




'''for odd in [1, 3, 5, 7]:
    print(odd*odd)'''



#Page 46

'''
def main():
    print("This program calculates the future \n value of a 10-year investment")
    principal = eval(input("Enter the initial principal: "))

#input the annual percentage rate

    apr = eval(input("Enter the annual interest rate: "))

    for i in range(10):
        principal = principal*(1+apr)

    print("The value in 10 years is:", principal)

main()'''


#LECTURE 3

'''type(3)'''


#Doesn't work:... unless the last number is negative
'''import math

def main():
    print("This program finds the real solutions to a quadratic")
    print()

    a, b, c = eval(input("Please enter the coefficients (a,b,c): "))

    discRoot = math.sqrt(b*b-4*a*c)

    root1 = (-b + discRoot)/(2*a)
    root2 = (-b - discRoot)/(2*a)

    print()
    print("The solutions are:", root1, root2)


main()'''

#page 24

'''fact = 1

for factor [6,5,4,3,2,1]:
    fact = fact*factor
    print(fact)'''



# my_list = list(range(10))
# print (my_list)



def main():
    
    n = eval(input("Enter a number: "))
    fact = 1
    for factor in range(n,1,-1):
        fact = fact*factor

    print(n, "factorial is", fact)

main ()
main()
