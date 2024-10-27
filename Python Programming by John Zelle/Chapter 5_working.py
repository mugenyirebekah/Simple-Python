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
