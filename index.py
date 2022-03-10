from tkinter import *
#importing all classes and functions from tkinter library
from tkinter.ttk import *
#importing all classes and functions from tkinter.ttk library
from time import *
#importing all classes and functions from time library
import random
#importing random library

#************************************************************************************************************************************************************************************

#program by Devansh Goel (GitHub:thequanic)

#************************************************************************************************************************************************************************************
def generate():
    #function to generate random temp_passwd

    max_len=12;
    #max length of temp_passwd
    numbers=['1','2','3','4','5','6','7','8','9','0']
    #list of numbers temp_passwd can contain 
    loweralpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','w','v','x','y','z']
    #list of lower case alphabet temp_passwd can contain
    upperalpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','W','V','X','Y','Z']
    #list of upper case alphabet temp_passwd can contain
    symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']
    #list of symbols temp_passwd can contain
    superlist=numbers+loweralpha+upperalpha+symbols
    #list of all characters temp_passwd can contain

    temp_passwd= random.choice(numbers)+random.choice(loweralpha)+random.choice(upperalpha)+random.choice(symbols)
    #temp_passwd of 4 characters containing 1 random number, 1 random lower case alpha
    # 1 random upper case alpha, 1 random symbol
    temp_passwd=list(temp_passwd)
    #converting temp_password from string to list so shuffle function can work on it

    for i in range(9):
        #for loop to add remaing 9 characters to password, randomly from superlist
        temp_passwd+=random.choice(superlist)
        random.shuffle(temp_passwd)
        #shuffling characters position
      

    password=str()
    #initialing empty string
        
    for i in range (13):
        #converting temp_list to string as password
        password+=temp_passwd[i]
        #adding elements of temp_password to password

    
    print(password)

#************************************************************************************************************************************************************************************
window=Tk()
#creating GUI window
window.geometry("700x500")
#defining size of GUI window
window.title("Random Password Generator")
#defing title of GUI window
window.configure(bg='blue')
#defining background color of GUI window

#************************************************************************************************************************************************************************************
msg=Message(window,text="WELCOME TO \nRANDOM PASSWORD GENERATOR",font=('callibri',24,'italic bold underline'),fg="yellow",bg="blue",width=600,justify=CENTER)
msg.pack()

text=Text(window,height=1, width=40)
text.pack()

button=Button(window,text="Generate Random Passwd")
button.pack()

'''
pb1=Progressbar(window,orient=HORIZONTAL,length=100,mode="determinate")
def f1():
    pb1["value"]=20
    window.update_idletasks()
    sleep(1)
    pb1["value"]=40
    window.update_idletasks()
    sleep(1)
    pb1["value"]=60
    window.update_idletasks()
    sleep(1)
    pb1["value"]=80
    window.update_idletasks()
    sleep(1)
    pb1["value"]=100
    window.update_idletasks()
    sleep(1)
#pb1.pack()'''

#************************************************************************************************************************************************************************************
window.mainloop()
#this will allow window to remain open until closed by user
#************************************************************************************************************************************************************************************
