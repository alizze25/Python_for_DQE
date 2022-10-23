from datetime import datetime
import random
import os
from HW_4_final import *
mainFilePAth = "C:\/Users\Alisa_Yavorska\PycharmProjects\Python_for_DQE\/news_feed.txt"
defaultFilePath = "C:\/Users\Alisa_Yavorska\PycharmProjects\Python_for_DQE\/weather.txt"
menu_options = {
    0: 'Create file and extension',
    1: 'Add news',
    2: 'Write advertising',
    3: 'Scary story',
    4: 'Weather forecast',
    5: 'Exit',
}
curDT = datetime.now()
curDT1 = datetime.now()
random_number = random.randint(1, 10)
file_name = ''
# current date
date_time = curDT.strftime("%m/%d/%Y")
def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def option0():
    global file_name
    file_name = input('Filename with extension, e.g. example.txt: ')
     #print('Handle option \'Add news\'')
def option1():
    #file_name = input('Filename with extension, e.g. example.txt: ')
    #with open(file_name, 'w', encoding='utf-8') as f:
    f = open(file_name, 'a', encoding='utf-8')
    f.write(input('News: '))
    f.write("\n")
    f.write(input('Text news: '))
    f.write("\n")
    f.write(input('City: '))
    f.write("\n")
    f.write(date_time)
    f.write("\n")
    f.close()
     #print('Handle option \'Add news\'')

def option2():
    #file_name = input('Filename with extension, e.g. example.txt: ')
    f = open(file_name, 'a', encoding='utf-8')
    f.write("\n")
    f.write("\n")
    f.write(input('Advert text: '))
    f.write("\n")
    n1 = input('Final date: ')
    f.write(n1)
    dt_obj = datetime.strptime(n1, '%m/%d/%Y')
    delta = dt_obj - curDT1
    f.write("\n")
    f.write('Days left: ')
    f.write(str(delta.days))
    f.write("\n")
    f.close()

def option3():
    #file_name = input('Filename with extension, e.g. example.txt: ')
    f = open(file_name, 'a', encoding='utf-8')
    f.write("\n")
    f.write("\n")
    f.write(input('What your name storyteller: '))
    f.write("\n")
    f.write(input('Tell me your story: '))
    f.write("\n")
    f.write('Horror points: ')
    f.write(str(random_number))
    f.write("\n")

def option4():
    file_path = input('Enter a file path: ')
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            lines = f.read()
        with open(mainFilePAth, 'a', encoding='utf-8-sig') as fullFIle:
            fullFIle.write("\n")
            fullFIle.write('Weather forecast: ')
            fullFIle.write("\n")
            fullFIle.write(Beautifyer(lines))
            os.remove(file_path)
    else:
        with open(defaultFilePath, 'r', encoding='utf-8-sig') as f:
            lines1 = f.read()
        with open(mainFilePAth, 'a', encoding='utf-8-sig') as fullFIle:
            fullFIle.write("\n")
            fullFIle.write('Weather forecast: ')
            fullFIle.write("\n")
            fullFIle.write(Beautifyer(lines1))
            #os.remove(defaultFilePath)
if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 0:
           option0()
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            option4()
        elif option == 5:
            print('Thanks message before exiting')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')