from pathlib import Path

import os

def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i , items in enumerate(items):
        print(f"{i + 1} : {items}")

def createfile():
    try:

        readfileandfolder()
        name = input("Enter your file name : ")
        p = Path(name)
        if not p.exists():

            with open(p ,'w') as fs:
                data = input("Enter what you want to write inside this file : ")
                fs.write(data)
        else:
            print("FILE ALREADY EXISTED!!!")
        print(f"FILE CREATED SUCCESSFULLY!!!")
    except Exception as err:
        print(f"There was an error as {err}!!")

def readfile():
    try:
        readfileandfolder()
        name = input("Which respective file you want to read : ")
        path = Path(name)
        if not p.exists() and p.is_file():
            with open(p , 'r') as fs:
                data = fs.read()
                print(data)
            print("FILE READ SUCCESSFULLY!!")
        else:
            print("File does not exists!!")
    except Exception as err:
        print(f"There was an error as {err}")

def updatefile():
    try:
        readfileandfolder()
        name = input("Which file you want to update : ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("Press 1 for changing the name of the file : ")
            print("Press 2 for overwriting the data of the respective file : ")
            print("Press 3 for appending some content to your file : ")

            response = int(input("Enter your choice of updating the file : "))

            if (response == 1):
                new_name = input("Tell me your new name for the file : ")
                path_2 = Path(new_name)
                p.rename(path_2)

            if (response == 2):
                with open(p , 'w') as fs:
                    data = input("Enter the contents you want to overwrite here : ")
                    fs.write(data)

                
            if (response == 3):
                with open(p , 'w') as fs:
                    data = input("Add your extra content here : ")
                    fs.write(" " + data)
    except Exception as err:
        print(f"There was an error as {err}")



def deletefile():
    try:
        readfileandfolder()
        name = input("Which file you want to be deleted : ")
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(name)

            print("FILE DELETED/REMOVED SUCCESSFULLY!!")

        else:
            print("There is no such file!!")
    except Exception as err:
        print(f"There was an error as {err}")



print("Press 1 for Creating a file : ")
print("Press 2 for Reading a file : ")
print("Press 1 for Updating a file : ")
print("Press 1 for Deletion  a file : ")

check = int(input("Enter your choice of file : "))

if (check == 1):
    createfile()


if (check == 2):
    readfile()

if (check == 3):
    updatefile()

if (check == 4):
    deletefile()