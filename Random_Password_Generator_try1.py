import random

#the lists for random selection

#str(ASCII_upercase)

character1_list = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

character2_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

character3_list = ['j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

character4_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

character5_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

character6_list = ['!', '@', '#', '$', '%', '^', '&', '*']






random_str1 = random.choice(character1_list)

random_str2 = random.choice(character2_list)

random_str3 = random.choice(character3_list)

random_str4 = random.choice(character4_list)

random_str5 = random.choice(character5_list)

random_str6 = random.choice(character6_list)




print ('Generated Password:' + str(random_str1)+ str(random_str6) + str(random_str2) + str(random_str3) + str(random_str4) + str(random_str5)+ str(random_str6))
