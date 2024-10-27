'''# username.py
#    Simple string processing program to generate usernames.
def main():
    print("This program generates computer usernames.\n")
    # get user’s first and last names
    first = input("Please enter your first name (all lowercase): ")
    last = input("Please enter your last name (all lowercase): ")
    # concatenate first initial with 7 chars of the last name.
    uname = first[0] + last[:7]
    # output the username
    print("Your username is:", uname)
main()'''




'''def main():
    fname = input("Firstname: ")
    lname = input("Lastname: ")

    print("You're username is: ", fname[0] + lname[:10])

main()'''


##########################################################
'''def main():
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"

    rm = eval(input("Enter the number corresponding to the month that you want: "))
    pos = ((rm-1)*3)

    monthAbbrev = months[pos:pos+3]

    print("The month is: ", monthAbbrev)

main()'''

############################################################

'''months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug","Sep", "Oct", "Nov", "Dec"]

reqMonth = eval(input("Enter the number that corresponds to the month...:"))

print (months[reqMonth-1])
'''

#ENCODER
'''
plaintext = input("Enter the message you would like to encode: ")

for i in plaintext:
    print(ord(i), end=" ")'''

#DECODER


'''
def main():
    print("This program converts a sequence of Unicode numbers into")
    print("the string of text that it represents.\n")
    # Get the message to encode
    inString = input("Please enter the Unicode-encoded message: ")
    # Loop through each substring and build Unicode message
    message = ""
    for numStr in inString.split():
        codeNum = eval(numStr)           # convert digits to a number
        message = message + chr(codeNum) # concatentate character to message
    print("\nThe decoded message is:", message)
main()'''


#DECODER 2
'''

def main():
    print("This program converts a sequence of Unicode numbers into")
    print("the string of text that it represents.\n")

    # Get the message to encode
    inString = input("Please enter the Unicode-encoded message: ")
    # Loop through each substring and build Unicode message
    chars = []
    
    for i in inString.split():
        codeNum = eval(i)             # convert digits to a number
        chars.append(chr(codeNum))         # accumulate new character
    message = "".join(chars)
    print("\nThe decoded message is:", message)

    main()
main()'''



'''

def main():
    cT= input("Enter the encoded message: ")
                    #convert each unicode to text
    pT = []         #array to store the message

    cT2 = cT.split()

    for i in cT2:
        cT3 = eval(i)
        pT.append(chr(cT3))

    message = " ".join(pT)
    
    print (message)

    main()

main()'''


'''
def main():
    txt = input("Enter the text you want to encode: ")      # Enter the text
    for i in txt:    #print using string method ord()
        print(ord(i), end=" ")

main()'''


'''
def main():
    cT = input("Please enter the text you want to decode: ")

    message = ""

    for i in cT.split():
        cT2 = eval(i)
        #print(chr(cT2))
        message = message + chr(cT2)

    print(message)

    main()

main()
'''
'''
def main():
    cT = input("Please enter the text you want to decode: ")

    m1 = []

    for i in cT.split():
        cT2 = eval(i)
        #print(chr(cT2))
        m1.append(chr(cT2))

    m2 = " ".join(m1)

    print(m2)

    main()

main()'''

###########################################################################
'''

# dateconvert.py
#    Converts a date in form "mm/dd/yyyy" to "month day, year"
def main():
    # get the date
    dateStr = input("Enter a date (mm/dd/yyyy): ")
    # split into components
    monthStr, dayStr, yearStr = dateStr.split("/")
    # convert monthStr to the month name
    months = ["January", "February", "March", "April",
              "May", "June", "July", "August",
              "September", "October", "November", "December"]
    monthStr = months[int(monthStr)-1]
    # output result in month day, year format
    print("The converted date is:", monthStr, dayStr+",", yearStr)
main()'''

##########################################################################
'''
def main():
    dateStr = input("Please enter a date in the format dd/mm/yy: ")        #Enter a date
    date, month, year = dateStr.split("/")                                 #split the date with accurate parameter
    
    months = ["January", "February", "March", "April", "May", "Joune", "July", "August", "September", "October", "November", "December"]

    pmonth = months[(int(month)-1)]

    print("The date is", pmonth, date, year)
    

main()'''


'''
# dateconvert2.py
#     Converts day month and year numbers into two date formats
def main():
    # get the day month and year
    day, month, year = eval(input("Please enter day, month, and year numbers: "))
    date1 = str(month)+"/"+str(day)+"/"+str(year)
    months = ["January", "February", "March", "April",
              "May", "June", "July", "August",
              "September", "October", "November", "December"]
    monthStr = months[month-1]
    date2 = monthStr+" " + str(day) + ", " + str(year)
    print("The date is", date1, "or", date2+".")
main()'''

#########################################################
