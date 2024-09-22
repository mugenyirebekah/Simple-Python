# Project Name: Random city to visit

#Project Description: 
# There's a list...and a city is randomly selected...

#21:32 Tue.July.2.2024



import random 

city_list = ['Vienna', 'Copenhagen', 'Zurich', 'Melbourne', 'Calgary', 'Geneva', 'Sydney', 
             'Vancouver', 'Osaka', 'Auckland', 'Tokyo', 'Shanghai', 'São Paulo', 'Cairo', 'Mumbai' ]

comments_list = ['...What a place...', '...You want to book the tickets now?', '...Lez gooo', '...1st class or business?', '...funny, that.', '...Does next week work?'] 

# Possibly interesting fact: I wrote Lez gooo instead of let's go, because the apostrophe messes up the code.

random_str = random.choice(city_list) 

random_str2 = random.choice(comments_list)

#random_str = random.choice(comments_list)

print ("Random city selected:"+ str(random_str)+ str(random_str2))


#Travel. (˘◡˘)


#<Black_Unicorn/>
