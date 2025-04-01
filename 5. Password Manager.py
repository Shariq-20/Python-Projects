# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 01:08:26 2025
@author: Shariq
"""

"""
the point of this to store and manage your passwords along with their user names 
and the account they are associated with in a text file. NOT saving the passwords in a plain 
file but will encrypt the text.

Left incomplete... Rewatch

"""
from cryptography.fernet import Fernet   # library allows to take a string of text and convert it into a random string of text.


''' to only use once
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:         # key.key is a special file formate
        key_file.write(key)'''

def key():
    file = open('key.key', "rb")
    key = file.read()
    file.close()
    return key


m_pwd = input("what is the master password? ")
key = load_key() + master_pwd.encode          #.encode() turns into bytes -  adding the master password in its bytes format to the key and using it as the password 
fer = Fernet(key)

# key + password + text to encrypt = random text therefore password + random text + key = text to encrypt   

# Key PLUS the password is what you need to use to encrypt the text


def add():
    name = input("Account: ")
    pwd = input("Password: ")
    
    # what we need to do is create a new file and add the passwords into it    
    with open ('password.txt', 'a' ) as f:           # 'a' means to append will append every new input. file has 3 modes W, R, A  
        f.write(name + "|" + pwd + "\n")                 # when you use with it allows you to use 


def view():
    with open ('password.txt', 'a' ) as f:
        for line in f.readlines():
           line.rstrip()                # this is to stop showing the \n space below each view output rstrip() strips the \n
           user, passw = data.split("|") # rather than it comming in one line, data split uses the pipe inputed (|) and splits the data from there 
           print("User: ", user, "Password:", passw)



# view or add password 
mode = input("Would you like to add a new password or view an existing password (view / add / quit)?:  ")

while True:
    if mode == "quit":
        break
    if mode == "view":
        view()                  # could have just written pass rather than view() but the is a cleaner method of writing code.
    elif mode == "add":
        add()
    else:
        print("invalid")
        continue
    

"""    
learnt

+  'a' means to append will append every new input. file has 3 modes W, R, A
    W = will clear file and open an entirly new one (Overide)
    R = read only file
    A = Append mode, allowes to add something at the end of a file or create a new file and then add
    
+ \n is a line break and tells the text editor to go to the next line

+  Pass litrally does nothing its just there to avoid indentation error 

+ rstrip() strips the \n 

+ data.split("xyz") splits the data and puts it into a list formate so it MSA|password -> [MSA, passwoed]
    allows you to select the data using the index

can use random and then a list to selet item from list

+ found a way to use (not in)

"""