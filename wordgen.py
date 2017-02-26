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

#initialize global variables
length=1
roll=0
roll1=0
roll2=0
count=0
con=""
tag=0
filename="default"

#set functions



#Die-rolling function
def dice(n,sides): #Input number of dice, sides per die
	die=0
	roll=0
	while die<n:
		roll=roll+random.randint(1,sides)
		die+=1
	return roll #Output die roll result

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
	
#consonant generation functions
def con1():
    roll1=0
    roll2=0
    con=""
    roll1=dice(1,6)
    roll2=dice(1,6)
    if roll1 in [1,2]:
        con="f"
    if roll1==3:
        con="ft"
    if roll1==4 and roll2<=4:
        con="ft"
    if roll1==4 and roll2>=5:
        con="h"
    if roll1>=5:
        con="h"
    return con

def con2():
    roll1=0
    roll2=0
    con=""
    roll1=dice(1,6)
    roll2=dice(1,6)
    if roll1==1 and roll2<=4:
        con="h"
    if roll1==1 and roll2>=5:
        con="hf"
    if roll1==2 and roll2<=4:
        con="hf"
    if roll1==2 and roll2>=5:
        con="hk"
    if roll1==3:
        con="hk"
    if roll1==4 and roll2<=3:
        con="hk"
    if roll1==4 and roll2>=4:
        con="hl"
    if roll1==5 and roll2<=5:
        con="hl"
    if roll1==5 and roll2==6:
        con="hr"
    if roll1==6:
        con="hr"
    return con

def con3():
    roll1=0
    roll2=0
    con=""
    roll1=dice(1,6)
    roll2=dice(1,6)
    if roll1 in [1, 2]:
        con="ht"
    if roll1==3 and roll2<=5:
        con="hw"
    if roll1==3 and roll2==6:
        con="k"
    if roll1 in [4, 5]:
        con="k"
    if roll1==6 and roll2<=4:
        con="k"
    if roll1==6 and roll2>=5:
        con="kh"
    return con

def con4():
    roll1=0
    roll2=0
    con=""
    roll1=dice(1,6)
    roll2=dice(1,6)
    if roll1 in [1,2]:
        con="kh"
    if roll1 in [3, 4]:
        con="kht"
    if roll1==5:
        con="kt"
    if roll1==6 and roll2<=4:
        con="kt"
    if roll1==6 and roll2>=5:
        con="l"
    return con

def con5():
    roll1=0
    roll2=0
    con=""
    roll1=dice(1,6)
    roll2=dice(1,6)
    if roll1==1 and roll2<=3:
        con="l"
    if roll1==1 and roll2>=4:
        con="r"
    if roll1==2 and roll2<=4:
        con="r"
    if roll1==2 and roll2>=5:
        con="s"
    if roll1==3:
        con="s"
    if roll1==4 and roll2<=2:
        con="s"
    if roll1==4 and roll2>=3:
        con="st"
    if roll1==5 and roll2<=3:
        con="st"
    if roll1==5 and roll2>=4:
        con="t"
    if roll1==6:
        con="t"
    return con

def con6():
    roll1=0
    roll2=0
    con=""
    roll1=dice(1,6)
    roll2=dice(1,6)
    if roll1==1:
        con="t"
    if roll1==2 and roll2<=5:
        con="t"
    if roll1==2 and roll2==6:
        con="tl"
    if roll1==3 and roll2<=4:
        con="tl"
    if roll1==3 and roll2>=5:
        con="tr"
    if roll1==4 and roll2<=3:
        con="tr"
    if roll1==4 and roll2>=4:
        con="w"
    if roll1 in [5, 6]:
        con="w"
    return con

#construct consonant
def consonant():
    roll=0
    consonant=""
    roll=dice(1,6)
    if roll==1:
        consonant=con1()
    if roll==2:
        consonant=con2()
    if roll==3:
        consonant=con3()
    if roll==4:
        consonant=con4()
    if roll==5:
        consonant=con5()
    if roll==6:
        consonant=con6()
    return consonant

#vowel generation functions
def vow1():
        roll1=0
        roll2=0
        vow="a"
        return vow

def vow2():
        roll1=0
        roll2=0
        vow=""
        roll1=dice(1,6)
        roll2=dice(1,6)
        if roll1==1 and roll2<=5:
                vow="a"
        if roll1==1 and roll2==6:
                vow="ai"
        if roll1==2:
                vow="ai"
        if roll1==3 and roll2<=4:
                vow="ai"
        if roll1==3 and roll2>=5:
                vow="ao"
        if roll1==4:
                vow="ao"
        if roll1==5 and roll2<=4:
                vow="au"
        if roll1==5 and roll2>=5:
                vow="e"
        if roll1==6:
                vow="e"
        return vow

def vow3():
        roll1=0
        roll2=0
        vow=""
        roll1=dice(1,6)
        roll2=dice(1,6)
        if roll1<=3:
                vow="e"
        if roll1>=4:
                vow="ea"
        return vow

def vow4():
        roll1=0
        roll2=0
        vow=""
        roll1=dice(1,6)
        roll2=dice(1,6)
        if roll1==1:
                vow="ea"
        if roll1 in [2,3]:
                vow="ei"
        if roll1==4 and roll2==1:
                vow="ei"
        if roll1==4 and roll2>=2:
                vow="i"
        if roll1==5:
                vow="i"
        if roll1==6 and roll2<=5:
                vow="i"
        if roll1==6 and roll2==6:
                vow="iy"
        return vow

def vow5():
        roll1=0
        roll2=0
        vow=""
        roll1=dice(1,6)
        roll2=dice(1,6)
        if roll1==1:
                vow="iy"
        if roll1==2 and roll2<=5:
                vow="iy"
        if roll1==2 and roll2==6:
                vow="o"
        if roll1==3:
                vow="o"
        if roll1==4 and roll2==1:
                vow="o"
        if roll1==4 and roll2>=2 and roll2<=5:
                vow="oa"
        if roll1==4 and roll2==6:
                vow="oi"
        if roll1==5:
                vow="oi"
        if roll1==6 and roll2==1:
                vow="oi"
        if roll1==6 and roll2>=2:
                vow="ou"
        return vow

def vow6():
        roll1=0
        roll2=0
        vow=""
        roll1=dice(1,6)
        roll2=dice(1,6)
        if roll1==1 and roll2<=4:
                vow="u"
        if roll1==1 and roll2>=4:
                vow="ua"
        if roll1==2 and roll2<=2:
                vow="ua"
        if roll1==2 and roll2>=3:
                vow="ui"
        if roll1==3:
                vow="ya"
        if roll1==4 and roll2<=2:
                vow="ya"
        if roll1==4 and roll2>=3:
                vow="ye"
        if roll1==5 and roll2<=4:
                vow="ye"
        if roll1==5 and roll2>=5:
                vow="yo"
        if roll1==6 and roll2<=2:
                vow="yo"
        if roll1==6 and roll2>=3:
                vow="yu"
        return vow

#construct vowel
def vowel():
    roll=0
    vowel=""
    roll=dice(1,6)
    if roll==1:
        vowel=vow1()
    if roll==2:
        vowel=vow2()
    if roll==3:
        vowel=vow3()
    if roll==4:
        vowel=vow4()
    if roll==5:
        vowel=vow5()
    if roll==6:
        vowel=vow6()
    return vowel

#final consonent generation functions
def fin1():
        roll1=0
        roll2=0
        fin=""
        roll1=dice(1,6)
        roll2=dice(1,6)
        fin="h"
        return fin

def fin2():
        roll1=0
        roll2=0
        fin=""
        roll1=dice(1,6)
        roll2=dice(1,6)
        if roll1==1:
                fin="h"
        if roll1==2 and roll2<=4:
                fin="h"
        if roll1==2 and roll2>=5:
                fin="kh"
        if roll1 in [3,4]:
                fin="kh"
        if roll1==5 and roll2<=4:
                fin="kh"
        if roll1==5 and roll2>=5:
                fin="l"
        if roll1==6:
                fin="l"
        return fin

def fin3():
        roll1=0
        roll2=0
        fin=""
        roll1=dice(1,6)
        roll2=dice(1,6)
        if roll1<=4:
                fin="l"
        if roll1>=5:
                fin="lr"
        return fin

def fin4():
        roll1=0
        roll2=0
        fin=""
        roll1=dice(1,6)
        roll2=dice(1,6)
        if roll1==1 and roll2<=2:
                fin="lr"
        if roll1==1 and roll2>=3:
                fin="r"
        if roll1>=2 and roll1<=4:
                fin="r"
        if roll1==5 and roll2==1:
                fin="r"
        if roll1==5 and roll2>=2:
                fin="rl"
        if roll1==6:
                fin="rl"
        return fin

def fin5():
        roll1=0
        roll2=0
        fin=""
        roll1=dice(1,6)
        roll2=dice(1,6)
        if roll1==1:
                fin="rl"
        if roll1==2 and roll2==1:
                fin="rl"
        if roll1==2 and roll2>=2:
                fin="s"
        if roll1>=3 and roll1<=5:
                fin="s"
        if roll1==6 and roll2==1:
                fin="s"
        if roll1==6 and roll2>=2:
                fin="w"
        return fin

def fin6():
        roll1=0
        roll2=0
        fin=""
        roll1=dice(1,6)
        roll2=dice(1,6)
        if roll1>=1 and roll1<=3:
                fin="w"
        if roll1==4 and roll2<=4:
                fin="w"
        if roll1==4 and roll2>=5:
                fin=""
        if roll1>=5:
                fin=""
        return fin

		
#construct final consonant
def final():
    roll=0
    final=""
    roll=dice(1,6)
    if roll==1:
        final=fin1()
    if roll==2:
        final=fin2()
    if roll==3:
        final=fin3()
    if roll==4:
        final=fin4()
    if roll==5:
        final=fin5()
    if roll==6:
        final=fin6()
    return final

#Aslan word generator
def wordgen(): 
    roll1=0
    roll2=0
    tag=0
    length=0
    iteration=1
    syl=""
    syl2=""
    syl3=""
    syl4=""
    final_word=""
    word=[]
    length=dice(1,6)
    while iteration<=length:
            if iteration==1 or tag==1: #if the first syllable in a word or a sylable after a vowel
                    tag=0
                    roll1=dice(1,6)
                    roll2=dice(1,6)
                    if roll1 in [1,2]:
                            syl=vowel()
                            tag=1
                    if roll1==3 and roll2==1:
                            syl=vowel()
                            tag=1
                    if roll1==3 and roll2>=2:
                            syl2=consonant()
                            syl3=vowel()
                            syl="%s%s" % (syl2, syl3)
                            tag=1
                    if roll1==4 and roll2<=4:
                            syl2=consonant()
                            syl3=vowel()
                            syl="%s%s" % (syl2, syl3)
                            tag=1
                    if roll1==4 and roll2>=5:
                            syl2=vowel()
                            syl3=final()
                            syl="%s%s" % (syl2, syl3)
                    if roll1==5:
                            syl2=vowel()
                            syl3=final()
                            syl="%s%s" % (syl2, syl3)
                    if roll1==6:
                            syl2=consonant()
                            syl3=vowel()
                            syl4=final()
                            syl="%s%s%s" % (syl2, syl3, syl4)
                    word.append(syl)
            if iteration>=2 or tag==0: #if the previous syllable ended with a consonant
                    tag=0
                    roll1=dice(1,6)
                    roll2=dice(1,6)
                    if roll1 in [1, 2]:
                            syl=vowel()
                    if roll1==3 and roll2<=3:
                            syl=vowel()
                    if roll1==3 and roll2>=4:
                            syl2=vowel()
                            syl3=final()
                            syl="%s%s" % (syl2, syl3)
                    if roll1>=4:
                            syl2=vowel()
                            syl3=final()
                            syl="%s%s" % (syl2, syl3)
                    word.append(syl)
            iteration=iteration+1
            final_word=str.join('', word)
    return final_word
    
#Old program body from 2010 - UNUSED NOW
#count=0
#outp=open("aslan.txt","w")
#while count<1000:
#    word=wordgen()
#    outp.write(word+'\r\n')
#    count=count+1
#    word=""
# outp.close()

def interactive:
    #New program body from 2017
    menu=1
    while menu == 1: #Program will always return to the menu unless exited
        os.system('cls')
        print ("")
        print ("Welcome to the Aslan Word Generator v1.0")
        print ("========================================")
        print ("Please choose an option:")
        print ("1 - Generate a single word")
        print ("2 - Generate multiple words")
        print ("3 - Generate a file with multiple words")
        print ("4 - About")
        print ("5 - Exit Program")
        print ("========================================")
        choice=input("Please enter your choice: ")
        if choice != 1 and choice != "1" and choice != 2 and choice != "2" and choice != 3 and choice != "3" and choice !=4 and choice != "4" and choice != 5 and choice != "5": #Upon inappropriate input
            print ("")
            print("Invalid Input")
            print ("")
        if choice in [1, "1"]: #Generate one word
            print ("")
            print(wordgen())
            print ("")
            print ("Press any key to continue")
            input()
        if choice in [2, "2"]: #Generate multiple words
            print ("")
            num=int(input("Please enter the number of words you wish to generate: "))
            print ("")
            while num >= count:
                print(wordgen())
                count=count+1
            print ("")
            print ("Press any key to continue")
            input()
        if choice in [3, "3"]: #Generate multiple worlds to a file
            name=savefile()
            outp=open(name + ".txt","w")
            num=int(input("Please enter the number of words you wish to generate: "))
            while num >= count:
                word=wordgen()
                outp.write(word+'\r\n')
                count=count+1
                word=""
            outp.close()
            print ("")
            print ("File generated.")
            print ("")
            print ("Press any key to continue")
            input()
        if choice in [4, "4"]: #Displays program information
            print ("")
            print("Aslan Word Generation for Classic Traveller")
            print("v1.2, February 18, 2017")
            print("This is open source code, feel free to use it for any purpose")
            print("contact the author at golan2072@gmail.com")
        if choice in [5, "5"]: #exit
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


