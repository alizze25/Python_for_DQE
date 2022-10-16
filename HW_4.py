# def greet_user(username):
#     print(f"hello, {username.title()}!")
#
# greet_user('Jessy')

import random
import string

def build_dict_func(merged_dict):

dicts_list = []
for x in range(0, random.randint(2, 10)):
    z = {}
    for i in range(0, random.randint(2, 10)):
        z[random.choice(string.ascii_lowercase)] = round(random.random()*100)
    dicts_list.append(z)
print(dicts_list)
merged_dict = {}
print(len(dicts_list))
for i in range(0, len(dicts_list)):
    for k, v in dicts_list[i].items():
        if merged_dict.get(k) is None:
            merged_dict[k] = v
        if v > merged_dict[k]:
            merged_dict[k] = v
print(merged_dict)
build_dict_func()
