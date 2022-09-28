
from random import randint

# initializing list
test_list = ["Alisa", "Kim", "Serge"]

# initializing range
i, j = 0, 100

family = dict()
for ele in test_list:
    # assigning random elements
    family[ele] = randint(i, j)

# printing result
print("Random range initialized dictionary : " + str(family))



# initializing list
home_pets = ["Cat", "Dog", "Lion", "Frog", "Mouse"]

# initializing range
i, j = 0, 100

pets = dict()
for ele in home_pets:
    # assigning random elements
    pets[ele] = randint(i, j)

# printing result
print("Random range initialized dictionary : " + str(pets))

# number 3 dictionary
largest_cities = ["Kyiv", "Kharkiv", "Odesa"]  #  create list cities
population = [2967360, 1443207, 1017699]  #  create list population
largest_cities_dict = dict(zip(largest_cities, population))  #  used the zip() function to concatenate our lists into a dictionary
print(largest_cities_dict)


 #  de-serializes the contents of dictionary to a collection of key/value pairs
main_dict = {**family, **pets, **largest_cities_dict}
print('Dictionary 3 :')
print(main_dict)



#  second homework assignment

# Each time there will be a different value for the number of dicts, dicts also with random keys and different lengths
import random
import string
dicts_list = []
for x in range(0, random.randint(2, 10)):
    z = {}
    for i in range(0, random.randint(2, 10)):
        z[random.choice(string.ascii_lowercase)] = round(random.random()*100)
    dicts_list.append(z)
print(dicts_list)


