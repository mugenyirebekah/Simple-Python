# Project Name: Random_Password_Generator

#Project Description: 
# There's a list...and a city is randomly selected...

#23:15 Fri.July.5.2024


import random



def shuffle(string):
    templist = list(string)
    random.shuffle(templist)
    return ''.join(templist)

uppercaseLetter1=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII)
uppercaseLetter2=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII)
lowercaseLetter1=chr(random.randint(97,122))
lowercaseLetter2=chr(random.randint(97,122))
character1=chr(random.randint (33,64))
character2=chr(random.randint (33,64))


password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + character1 + character2 + uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + character1 + character2
password = shuffle(password)

print(password)

#<Black_Unicorn/>
