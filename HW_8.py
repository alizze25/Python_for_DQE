# Description
# Expand previous Homework 5/6/7 with additional class, which allow to provide records by JSON file:
# 1.Define your input format (one or many records)
# 2.Default folder or user provided file path
# 3.Remove file if it was successfully processed


# hw_7
from datetime import datetime
import random
import json
import os
from collections import Counter
from operator import itemgetter
import re
import csv
from HW_4_final import *

mainFilePAth = "C:\/Users\Alisa_Yavorska\PycharmProjects\Python_for_DQE\/news_feed.txt"
defaultFilePath = "C:\/Users\Alisa_Yavorska\PycharmProjects\Python_for_DQE\/weather.txt"
fn = ("C:\/Users\Alisa_Yavorska\PycharmProjects\Python_for_DQE\/news_feed.txt")
menu_options = {
    0: 'Create file and extension',
    1: 'Add news',
    2: 'Write advertising',
    3: 'Scary story',
    4: 'Weather forecast',
    5: 'Json Data',
    6: 'Exit',
}
curDT = datetime.now()
curDT1 = datetime.now()
random_number = random.randint(1, 10)
file_name = 'news_feed.txt'
# current date
date_time = curDT.strftime("%m/%d/%Y")


def print_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


def create_file():
    global file_name
    file_name = input('Filename with extension, e.g. example.txt: ')
    # print('Handle option \'Add news\'')


def write_news():
    # file_name = input('Filename with extension, e.g. example.txt: ')
    # with open(file_name, 'w', encoding='utf-8') as f:
    f = open(file_name, 'a', encoding='utf-8')
    f.write(input('News: '))
    f.write("\n")
    f.write(input('Text news: '))
    f.write("\n")
    f.write(input('City: '))
    f.write("\n")
    f.write(date_time)
    f.write("\n")
    f.write("\n")
    f.close()
    # Count words
    try:
        os.remove("wordCount.csv")
        os.remove("count_all_file.csv")
    except OSError:
        pass
    text = open("news_feed.txt", "r")

    # Create an empty dictionary
    d = dict()

    # Loop through each line of the file
    for line in text:
        # Remove the leading spaces and newline character
        line = line.strip()

        # Convert the characters in line to
        # lowercase to avoid case mismatch
        line = line.lower()

        # Split the line into words
        words = line.split(" ")

        # Iterate over each word in line
        for word in words:
            # Check if the word is already in dictionary
            if word in d:
                # Increment count of word by 1
                d[word] = d[word] + 1
            else:
                # Add the word to dictionary with count 1
                d[word] = 1

            # Print the contents of dictionary
            # for key in list(d.keys()):
            # print(key, ":", d[key])

            # deleting the csv file

            f = open("wordCount.csv", "a", encoding='UTF8')
            for key in list(d.keys()):
                f.write(str(key))
                f.write(":")
                f.write(str(d[key]))
                f.write("\n")
    # Create second csv file
    file = open("C:\/Users\Alisa_Yavorska\PycharmProjects\Python_for_DQE\/news_feed.txt", "r")
    data = file.read()
    # get the length of the data
    number_of_characters = len(data)

    print('Number of characters in text file :', number_of_characters)

    # count_uppercase

    with open("news_feed.txt") as file:
        count = 0
        text = file.read()
        for i in text:
            if i.isupper():
                count += 1
        print(count)

        file = open("news_feed.txt", "rt")
        data = file.read()
        words = data.split()

        print('Number of words in text file :', len(words))

        # count percentage
        # text = "Alice opened the door and found that it led into a small passage, not much larger than a rat-hole: she knelt down and looked along the passage into the loveliest garden you ever saw."
        with open(fn) as f:
            data2 = f.read()
            # concatenating using join
            joined = " ".join(ele for ele in data2)

            # mapping using Counter()
            mappd = Counter(joined.split())

            # getting total using sum
            total_val = sum(mappd.values())

            # getting share of each word
            res = {key: val / total_val for key,
                                            val in mappd.items()}

            # printing result
            print("Percentage share of each word : " + str(res))

        # Write to csv
        with open('count_all_file.csv', 'w', newline='') as outcsv:
            writer = csv.writer(outcsv)
            writer.writerow(["Letters count", "All words count", "Uppercase count", "Percentage count"])
            writer.writerow([number_of_characters, len(words), count, str(res)])


def write_ads():
    # file_name = input('Filename with extension, e.g. example.txt: ')
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
    # Count words
    try:
        os.remove("wordCount.csv")
        os.remove("count_all_file.csv")
    except OSError:
        pass
    text = open("news_feed.txt", "r")

    # Create an empty dictionary
    d = dict()

    # Loop through each line of the file
    for line in text:
        # Remove the leading spaces and newline character
        line = line.strip()

        # Convert the characters in line to
        # lowercase to avoid case mismatch
        line = line.lower()

        # Split the line into words
        words = line.split(" ")

        # Iterate over each word in line
        for word in words:
            # Check if the word is already in dictionary
            if word in d:
                # Increment count of word by 1
                d[word] = d[word] + 1
            else:
                # Add the word to dictionary with count 1
                d[word] = 1

            # Print the contents of dictionary
            # for key in list(d.keys()):
            # print(key, ":", d[key])

            # deleting the csv file

            f = open("wordCount.csv", "a", encoding='UTF8')
            for key in list(d.keys()):
                f.write(str(key))
                f.write(":")
                f.write(str(d[key]))
                f.write("\n")
            # Create second csv file
            file = open("C:\/Users\Alisa_Yavorska\PycharmProjects\Python_for_DQE\/news_feed.txt", "r")
            data = file.read()
            # get the length of the data
            number_of_characters = len(data)

            print('Number of characters in text file :', number_of_characters)

            # count_uppercase

            with open("news_feed.txt") as file:
                count = 0
                text = file.read()
                for i in text:
                    if i.isupper():
                        count += 1
                print(count)

                file = open("news_feed.txt", "rt")
                data = file.read()
                words = data.split()

                print('Number of words in text file :', len(words))

                # count percentage
                # text = "Alice opened the door and found that it led into a small passage, not much larger than a rat-hole: she knelt down and looked along the passage into the loveliest garden you ever saw."
                with open(fn) as f:
                    data2 = f.read()
                    # concatenating using join
                    joined = " ".join(ele for ele in data2)

                    # mapping using Counter()
                    mappd = Counter(joined.split())

                    # getting total using sum
                    total_val = sum(mappd.values())

                    # getting share of each word
                    res = {key: val / total_val for key,
                                                    val in mappd.items()}

                    # printing result
                    print("Percentage share of each word : " + str(res))

                # Write to csv
                with open('count_all_file.csv', 'w', newline='') as outcsv:
                    writer = csv.writer(outcsv)
                    writer.writerow(["Letters count", "All words count", "Uppercase count", "Percentage count"])
                    writer.writerow([number_of_characters, len(words), count, str(res)])


def write_scarystory():
    # file_name = input('Filename with extension, e.g. example.txt: ')
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
    f.close()
    # Count words
    try:
        os.remove("wordCount.csv")
        os.remove("count_all_file.csv")
    except OSError:
        pass
    text = open("news_feed.txt", "r")

    # Create an empty dictionary
    d = dict()

    # Loop through each line of the file
    for line in text:
        # Remove the leading spaces and newline character
        line = line.strip()

        # Convert the characters in line to
        # lowercase to avoid case mismatch
        line = line.lower()

        # Split the line into words
        words = line.split(" ")

        # Iterate over each word in line
        for word in words:
            # Check if the word is already in dictionary
            if word in d:
                # Increment count of word by 1
                d[word] = d[word] + 1
            else:
                # Add the word to dictionary with count 1
                d[word] = 1

            # Print the contents of dictionary
            # for key in list(d.keys()):
            # print(key, ":", d[key])

            # deleting the csv file

            f = open("wordCount.csv", "a", encoding='UTF8')
            for key in list(d.keys()):
                f.write(str(key))
                f.write(":")
                f.write(str(d[key]))
                f.write("\n")

    # Create second csv file
    file = open("C:\/Users\Alisa_Yavorska\PycharmProjects\Python_for_DQE\/news_feed.txt", "r")
    data = file.read()
    # get the length of the data
    number_of_characters = len(data)

    print('Number of characters in text file :', number_of_characters)

    # count_uppercase

    with open("news_feed.txt") as file:
        count = 0
        text = file.read()
    for i in text:
        if i.isupper():
            count += 1
            print(count)

    file = open("news_feed.txt", "rt")
    data = file.read()
    words = data.split()

    print('Number of words in text file :', len(words))

    # count percentage
    with open(fn) as f:
        data2 = f.read()
        # concatenating using join
        joined = " ".join(ele for ele in data2)

        # mapping using Counter()
        mappd = Counter(joined.split())

        # getting total using sum
        total_val = sum(mappd.values())

        # getting share of each word
        res = {key: val / total_val for key, val in mappd.items()}

        # printing result
        print("Percentage share of each word : " + str(res))

        # Write to csv
        with open('count_all_file.csv', 'w', newline='') as outcsv:
            writer = csv.writer(outcsv)
            writer.writerow(["Letters count", "All words count", "Uppercase count", "Percentage count"])
            writer.writerow([number_of_characters, len(words), count, str(res)])


def write_weather():
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
            # os.remove(defaultFilePath)
            # Count words
            try:
                os.remove("wordCount.csv")
                os.remove("count_all_file.csv")
            except OSError:
                pass
            text = open("news_feed.txt", "r")

            # Create an empty dictionary
            d = dict()

            # Loop through each line of the file
            for line in text:
                # Remove the leading spaces and newline character
                line = line.strip()

                # Convert the characters in line to
                # lowercase to avoid case mismatch
                line = line.lower()

                # Split the line into words
                words = line.split(" ")

                # Iterate over each word in line
                for word in words:
                    # Check if the word is already in dictionary
                    if word in d:
                        # Increment count of word by 1
                        d[word] = d[word] + 1
                    else:
                        # Add the word to dictionary with count 1
                        d[word] = 1

                    # Print the contents of dictionary
                    # for key in list(d.keys()):
                    # print(key, ":", d[key])

                    # deleting the csv file

                    f = open("wordCount.csv", "a", encoding='UTF8')
                    for key in list(d.keys()):
                        f.write(str(key))
                        f.write(":")
                        f.write(str(d[key]))
                        f.write("\n")

    # Create second csv file
    file = open("C:\/Users\Alisa_Yavorska\PycharmProjects\Python_for_DQE\/news_feed.txt", "r")
    data = file.read()
    # get the length of the data
    number_of_characters = len(data)

    print('Number of characters in text file :', number_of_characters)

    # count_uppercase

    with open("news_feed.txt") as file:
        count = 0
        text = file.read()
    for i in text:
        if i.isupper():
            count += 1
            print(count)

    file = open("news_feed.txt", "rt")
    data = file.read()
    words = data.split()

    print('Number of words in text file :', len(words))

    # count percentage
    with open(fn) as f:
        data2 = f.read()
        # concatenating using join
        joined = " ".join(ele for ele in data2)

        # mapping using Counter()
        mappd = Counter(joined.split())

        # getting total using sum
        total_val = sum(mappd.values())

        # getting share of each word
        res = {key: val / total_val for key, val in mappd.items()}

        # printing result
        print("Percentage share of each word : " + str(res))

        # Write to csv
        with open('count_all_file.csv', 'w', newline='') as outcsv:
            writer = csv.writer(outcsv)
            writer.writerow(["Letters count", "All words count", "Uppercase count", "Percentage count"])
            writer.writerow([number_of_characters, len(words), count, str(res)])


def write_jsondata():
    json_path = input('Enter valid json path: ')
    if os.path.exists(json_path):
        with open(json_path, 'r') as openfile:
            f = open(file_name, 'a', encoding='utf-8')
            f.write("\n")

            #  Reading from json file
            # resp = json.dumps(openfile.__dict__)
            # o = json.loads(resp)
            data = json.load(openfile)
        if 'row1' in data:
            for i in data['row1']:
                if i['type1'] == "news":
                    f.write("Name: ")
                    f.write(i['type1'])
                    f.write("\n")
                    f.write("Text: ")
                    f.write(i['text_news'])
                    f.write("\n")
                    f.write("From: ")
                    f.write(i['city'])
                    f.write("\n")

                elif i['type1'] == "ads":
                    f.write("Type: ")
                    f.write(i['type1'])
                    f.write("\n")
                    f.write("ads_text: ")
                    f.write(i['ads_text'])
                    f.write("\n")
                    f.write("ads_date: ")
                    f.write(i['ads_date'])
                    f.write("\n")
                    print()

        if 'row2' in data:
            for i in data['row2']:
                if i['type2'] == "news":
                    f.write("\n")
                    f.write("Name: ")
                    f.write(i['type2'])
                    f.write("\n")
                    f.write("Text: ")
                    f.write(i['text_news'])
                    f.write("\n")
                    f.write("From: ")
                    f.write(i['city'])
                    f.write("\n")
                elif i['type2'] == "ads":
                    f.write("\n")
                    f.write("Type: ")
                    f.write(i['type2'])
                    f.write("\n")
                    f.write("ads_text: ")
                    f.write(i['ads_text'])
                    f.write("\n")
                    f.write("ads_date: ")
                    f.write(i['ads_date'])
                    f.write("\n")
        else:
            print("Invalid json")
    else:
        with open('try.json', 'r') as openfile:
            data = json.load(openfile)
            f = open(file_name, 'a', encoding='utf-8')
            f.write("\n")
        if 'row1' in data:
            for i in data['row1']:
                if i['type1'] == "news":
                    f.write("Name: ")
                    f.write(i['type1'])
                    f.write("\n")
                    f.write("Text: ")
                    f.write(i['text_news'])
                    f.write("\n")
                    f.write("From: ")
                    f.write(i['city'])
                    f.write("\n")

                elif i['type1'] == "ads":
                    f.write("Type: ")
                    f.write(i['type1'])
                    f.write("\n")
                    f.write("ads_text: ")
                    f.write(i['ads_text'])
                    f.write("\n")
                    f.write("ads_date: ")
                    f.write(i['ads_date'])
                    f.write("\n")
                    print()

        if 'row2' in data:
            for i in data['row2']:
                if i['type2'] == "news":
                    f.write("\n")
                    f.write("Name: ")
                    f.write(i['type2'])
                    f.write("\n")
                    f.write("Text: ")
                    f.write(i['text_news'])
                    f.write("\n")
                    f.write("From: ")
                    f.write(i['city'])
                    f.write("\n")
                elif i['type2'] == "ads":
                    f.write("\n")
                    f.write("Type: ")
                    f.write(i['type2'])
                    f.write("\n")
                    f.write("ads_text: ")
                    f.write(i['ads_text'])
                    f.write("\n")
                    f.write("ads_date: ")
                    f.write(i['ads_date'])
                    f.write("\n")
        else:
            print("Invalid json")

# Count words
    try:
        os.remove("wordCount.csv")
        os.remove("count_all_file.csv")
    except OSError:
        pass
    text = open("news_feed.txt", "r")

    # Create an empty dictionary
    d = dict()

    # Loop through each line of the file
    for line in text:
        # Remove the leading spaces and newline character
        line = line.strip()

        # Convert the characters in line to
        # lowercase to avoid case mismatch
        line = line.lower()

        # Split the line into words
        words = line.split(" ")

        # Iterate over each word in line
        for word in words:
            # Check if the word is already in dictionary
            if word in d:
                # Increment count of word by 1
                d[word] = d[word] + 1
            else:
                # Add the word to dictionary with count 1
                d[word] = 1

            # Print the contents of dictionary
            # for key in list(d.keys()):
            # print(key, ":", d[key])

            # deleting the csv file

            f = open("wordCount.csv", "a", encoding='UTF8')
            for key in list(d.keys()):
                f.write(str(key))
                f.write(":")
                f.write(str(d[key]))
                f.write("\n")
            # Create second csv file
            file = open("C:\/Users\Alisa_Yavorska\PycharmProjects\Python_for_DQE\/news_feed.txt", "r")
            data = file.read()
            # get the length of the data
            number_of_characters = len(data)

            print('Number of characters in text file :', number_of_characters)

            # count_uppercase

            with open("news_feed.txt") as file:
                count = 0
                text = file.read()
                for i in text:
                    if i.isupper():
                        count += 1
                print(count)

                file = open("news_feed.txt", "rt")
                data = file.read()
                words = data.split()

                print('Number of words in text file :', len(words))

                # count percentage
                # text = "Alice opened the door and found that it led into a small passage, not much larger than a rat-hole: she knelt down and looked along the passage into the loveliest garden you ever saw."
                with open(fn) as f:
                    data2 = f.read()
                    # concatenating using join
                    joined = " ".join(ele for ele in data2)

                    # mapping using Counter()
                    mappd = Counter(joined.split())

                    # getting total using sum
                    total_val = sum(mappd.values())

                    # getting share of each word
                    res = {key: val / total_val for key,
                                                    val in mappd.items()}

                    # printing result
                    print("Percentage share of each word : " + str(res))

                # Write to csv
                with open('count_all_file.csv', 'w', newline='') as outcsv:
                    writer = csv.writer(outcsv)
                    writer.writerow(["Letters count", "All words count", "Uppercase count", "Percentage count"])
                    writer.writerow([number_of_characters, len(words), count, str(res)])

if __name__ == '__main__':
    while (True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        # Check what choice was entered and act accordingly
        if option == 0:
            create_file()
        if option == 1:
            write_news()
        elif option == 2:
            write_ads()
        elif option == 3:
            write_scarystory()
        elif option == 4:
            write_weather()
        elif option == 5:
            write_jsondata()
        elif option == 6:
            print('Thanks message before exiting')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 6.')
