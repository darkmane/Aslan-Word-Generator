#! /usr/bin/python
#Wordgen.py
#Word Generation for Classic Traveller
# v1.3, February 27, 2017
# This is open source code, feel free to use it for any purpose
# contact the author at golan2072@gmail.com

#import modules
import random
import string
import os
import argparse
import json

#initialize global variables
length=1
roll=0
roll1=0
roll2=0
count=0
con=""
tag=0
filename="default"

PATH="traveller_data/lbb/%s"
ASLAN="am1/27.json"
KKREE="am2/17.json"
VARGR="am3/14.json"
ZHODANI="am4/21.json"
DROYNE="am5/41.json"
DARRIAN="am8/31.json"
LANGUAGE_LIST = [ASLAN, KKREE, VARGR, ZHODANI, DROYNE, DARRIAN]


class WordGenTable:
    def __init__(self, language):
        self.data_table = []
        if !(language in LANGUAGE_LIST):
            throw new Exception('Invalid language')

        self.__lang = language
        file_path = (PATH) % (language)
        print file_path
        with open(file_path) as data_file
            self.data_table = data_file['data']

    def language(self):
        language = ''
        if self.__lang == ASLAN:
            language = 'Aslan'

        if self.__lang == KKREE:
            language = 'K\'kree'
        if self.__lang == VARGR:
            language = 'Vargr'
        if self.__lang == ZHODANI
            language = 'Zhodani'
        if self.__lang == DROYNE:
            language = 'Droyne'
        if self.__lang == DARRIAN:
            language = 'Darrian'

        return language


    def generate_word:
        num_syllables = random.randint(1,6)
        word = ''
        syllable_count = 0
        syllable_func = basic_syllable

        for syllable_count++ < num_syllables:
            d1 = random.randint(1,6)
            d2 = random.randint(1,6)
            syllable_pattern = syllable_func(d1, d2)
            if syllable_pattern[len(syllable_pattern) -1] = 'V':
                syllable_func = basic_syllable
            else:
                syllable_fun = alternate_syllable

            consonant = initial_consonant
            phoneme_counter = 0
            while phoneme_counter < len(syllable_pattern):
                d1 = random.randint(1, 6)
                d2 = random.randint(1, 6)
                d3 = random.randint(1, 6)
                if syllable_pattern[phoneme_counter] = 'V':
                    word = ''.join([word, vowel(d1, d2, d3)])
                else:
                    word = ''.join([word, consonant(d1, d2, d3)])

                consonant = final_consonant

        return word

                

    def basic_syllable(d1, d2):
        return self.data_table['syllables']['basic'][d1][d2]

    def alternate_syllable(d1, d2):
        return self.data_table['syllables']['alternate'][d1][d2]

    def initial_consonant(d1, d2, d3):
        return self.data_table['phonemes']['initial_consonant'][d1][d2][d3]

    def vowel(d1, d2, d3):
        return self.data_table['phonemes']['vowel'][d1][d2][d3]

    def final_consonant(d1, d2, d3):
        return self.data_table['phonemes']['final_consonant'][d1][d2][d3]


#set functions

#Simple yes or no prompt filtering invalid results
def yn():
	query = 1
	while query == 1:
		answer = input("Y/N: ")
		if answer in ["y", "Y"]:
			return "y"
			query = 0
		if answer in ["y", "Y"]:
			return "n" #Output: "y" or "n"
			query = 0
		else:
			print ("Invalid Answer")
	
#File-saving function
def savefile():
	filename=str(input("Please enter file name to generate: "))
	directory=os.listdir(".\\") #Check if file already exists
	save=1
	filecheck=filename+".txt"
	if filecheck in directory: #Overwrite query
		while save == 1:
			print(" ")
			print("File already exists. Overwrite?")
			overwrite=yn()
			if overwrite == "y":
				save=0
				break
			if overwrite == "n":
				filename=input("Please enter new file name to generate: ")
	return filename #Output: file name

def interactive:
    word_gen_table = new WordGenTable(ASLAN)
    #New program body from 2017
    menu=1
    while menu == 1: #Program will always return to the menu unless exited
        os.system('cls')
        print ("")
        print ("Welcome to the Traveller Word Generator v1.0")
        print ("Current Language: " + word_gen_table.language())
        print ("========================================")
        print ("Please choose an option:")
        print ("1 - Generate a single word")
        print ("2 - Generate multiple words")
        print ("3 - Generate a file with multiple words")
        print ("4 - Change language")
        print ("5 - About")
        print ("6 - Exit Program")
        print ("========================================")
        choice=input("Please enter your choice: ")
        try:
            choice = int(choice)
        except Exception:
            print ("")
            print("Invalid Input")
            print ("")
            next

        if choice < 1 or choice > 6: #Upon inappropriate input
            print ("")
            print("Invalid Input")
            print ("")
        if choice == 1: #Generate one word
            print ("")
            print(word_gen_table.generate_word())
            print ("")
            print ("Press any key to continue")
            input()
        if choice == 2: #Generate multiple words
            print ("")
            num=int(input("Please enter the number of words you wish to generate: "))
            print ("")
            while num >= count:
                print(word_gen_table.generate_word())
                count=count+1
            print ("")
            print ("Press any key to continue")
            input()
        if choice == 3: #Generate multiple worlds to a file
            name=savefile()
            outp=open(name + ".txt","w")
            num=int(input("Please enter the number of words you wish to generate: "))
            while num >= count:
                word= word_gen_table.generate_word()
                outp.write(word+'\r\n')
                count=count+1
                word=""
            outp.close()
            print ("")
            print ("File generated.")
            print ("")
            print ("Press any key to continue")
            input()
        if choice == 4:
            print ("")
            print ("Welcome to the Traveller Word Generator v1.3")
            print ("========================================")
            print ("Please choose new language:")
            print ("1 - Generate Aslan words")
            print ("2 - Generate K'kree words")
            print ("3 - Generate Vargr words")
            print ("4 - Generate Zhodani words")
            print ("5 - Generate Droyne words")
            print ("6 - Generate Darrian words")
            print ("========================================")
            choice2 = input()
            try:
                choice2 = int(choice2)
            except Exception:
                print ("")
                print("Invalid Input")
                print ("")

            word_gen_table = WordGenTable(LANGUAGE_LIST[choice2 - 1])            


            
        if choice == 5: #Displays program information
            print ("")
            print("Word Generation for Classic Traveller")
            print("v1.3, February 27, 2017")
            print("This is open source code, feel free to use it for any purpose")
            print("contact the author at darkmane@gmail.com")
        if choice == 6: #exit
            menu=0
            break

if __name__ == "__main__":
    import argparser
    parser = argparse.ArgumentParser(description='Generate alien words')

    parser.add_argument('--language', '-l', type=str)
    parser.add_argument('--input', '-i', type=str)
    parser.add_argument('--output', '-o', type=str)
    parser.add_argument('--wordcount', '-w', type=int)
    parser.add_argument('--interactive', '-I', type=bool)


