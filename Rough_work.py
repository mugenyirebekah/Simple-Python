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

'''def calc_yaka():
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

main()'''

#--------------------------------OR--------------------------#


def calc_yaka():
    amount_paid = 8000
    units = amount_paid/560
    return units

def calc_water():
    units_consumed = 990
    units_cost = units_consumed*4100
    return units_cost


def main():
    print(f"You have {units} yaka units")
    print(f"You owe {units_cost} for water.")


####################################################
