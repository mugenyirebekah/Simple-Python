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
