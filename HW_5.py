menu_options = {
    0: 'Create file and extension',
    1: 'Add news',
    2: 'Write advertising',
    3: 'Scary story',
    4: 'Exit',
}
String file_name
def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def option0():
    file_name = input('Filename with extension, e.g. example.txt: ')
     #print('Handle option \'Add news\'')
def option1():
    

    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(input('Your message: '))
     #print('Handle option \'Add news\'')

def option2():
     print('Handle option \'Write advertising\'')

def option3():
     print('Handle option \'Scary story\'')

if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            print('Thanks message before exiting')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')