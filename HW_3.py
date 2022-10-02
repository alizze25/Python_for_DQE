
import string
s = '''Description
homEwork:
  tHis iz your homeWork, copy these Text to variable.
  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.
  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.
  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''

u = s.lower() # lower all text

word = u[0].title()  + u[1:]  # #split text into 2 parts and apply title function to first word
print(word)
x = word
try1 = '\n'.join([i.strip().capitalize() for i in x.split('.')]) #Capitalize all first words after period and start from new line\
print(try1)
x12 = try1.replace("iz", "is")
print(x12)
x13 = x12.replace("normalise", "normalize")
print(x13)


# check count whitespace

#Program for counting number of spaces in text

c=0
for i in s:
	if(i.isspace()):
		c+=1
print("Number of Spaces : "+str(c))




