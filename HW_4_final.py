#  add func for hw3

import string
import re

sText = '''homEwork:
  tHis iz your homeWork, copy these Text to variable.
  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.
  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.
  last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''
def Beautifyer(s):
    u = s.lower()  # lower all text

    word = u[0].title() + u[1:]  # #split text into 2 parts and apply title function to first word
    print(word)
    x = word
    try1 = '\n'.join(
        [i.strip().capitalize() for i in
         x.split(';')])  # Capitalize all first words after period and start from new line\
    print(try1)
    x12 = try1.replace("iz", "is")
    print(x12)
    x13 = x12.replace("normalise", "normalize")
    print(x13)

    # check count whitespace

    # Program for counting number of spaces in text

    c = 0
    for i in s:
        if (i.isspace()):
            c += 1
    print("Number of Spaces : " + str(c))

    # Create one sentences with last words

    z = re.findall(r'(\w+)\.', try1)
    print(z)
    for i in z:
        try1 = try1 + ' ' + i
    print(try1)


Beautifyer(sText)
# check count whitespace

# Program for counting number of spaces in text
#Beautifyer(sText)



#  add func for hw2

# Each time there will be a different value for the number of dicts, dicts also with random keys and different lengths
def dict_func():
    import random
    import string
    dicts_list = []
    for x in range(0, random.randint(2, 10)):
        z = {}
        for i in range(0, random.randint(2, 10)):
            z[random.choice(string.ascii_lowercase)] = round(random.random() * 100)
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
dict_func()