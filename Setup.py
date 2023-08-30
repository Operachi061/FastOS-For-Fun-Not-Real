import os
import time
import shutil

Information = """           #############################################################################################
           ##                                                                                         ##
           ##                             THIS IS A FAKE OPERATING SYSTEM                             ##
           ##    THE FILES INSTALLED HERE WILL BE IN THIS FOLDER BUT WILL NOT BE TRUE SYSTEM FILES    ##
           ##                               FastOS IS MADE ONLY FOR FUN                               ##
           ##                           DO YOU WANT TO CONTINUE INSTALLATION?                         ##
           ##                                                                                         ##
           #############################################################################################"""
print(Information)
Quest = input("Yes or No: ")
if (Quest == "Yes"):
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    os.system("git clone https://github.com/HeheYolo/FastOS-For-Fun-Not-Real.git")
    shutil.move("./FastOS-For-Fun-Not-Real/.git", "./TrashFilesToDelete")
    shutil.move("./FastOS-For-Fun-Not-Real/.gitignore", "./TrashFilesToDelete")
    shutil.move("./FastOS-For-Fun-Not-Real/README.md", "./TrashFilesToDelete")
    os.mkdir("./src")
    shutil.move ("./FastOS-For-Fun-Not-Real/src/FastOS-Bootloader.cpp", "./src")
    shutil.move ("./FastOS-For-Fun-Not-Real/src/FastOS-Shell.cpp", "./src")
    os.rmdir("./FastOS-For-Fun-Not-Real/src")
    os.rmdir("./FastOS-For-Fun-Not-Real/")
    print("Compiling: FastOS-Shell")
    if os.system("g++ ./src/FastOS-Shell.cpp") == 0:
        print("Done!")
    else:
        print ("Error")
    os.rename(r"./a.exe",r"./FastOS-Shell.exe" )
    print("Compiling: FastOS-Bootloader")
    if os.system("g++ ./src/FastOS-Bootloader.cpp") == 0:
        print("Done!")
    else:
        print ("Error")
    os.rename(r"./a.exe",r"./FastOS-Bootloader.exe" )
    print("Finish!")
    print("Start FastOS by typing: ./FastOS-Bootloader.exe or in linux/macos ./FastOS-Bootloader")

if (Quest == "No"):
    print("Canceled")
if (Quest == "yes"):
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    os.system("git clone https://github.com/HeheYolo/FastOS-For-Fun-Not-Real.git")
    shutil.move("./FastOS-For-Fun-Not-Real/.git", "./TrashFilesToDelete")
    shutil.move("./FastOS-For-Fun-Not-Real/.gitignore", "./TrashFilesToDelete")
    shutil.move("./FastOS-For-Fun-Not-Real/README.md", "./TrashFilesToDelete")
    os.mkdir("./src")
    shutil.move ("./FastOS-For-Fun-Not-Real/src/FastOS-Bootloader.cpp", "./src")
    shutil.move ("./FastOS-For-Fun-Not-Real/src/FastOS-Shell.cpp", "./src")
    os.rmdir("./FastOS-For-Fun-Not-Real/src")
    os.rmdir("./FastOS-For-Fun-Not-Real/")
    print("Compiling: FastOS-Shell")
    if os.system("g++ ./src/FastOS-Shell.cpp") == 0:
        print("Done!")
    else:
        print ("Error")
    os.rename(r"./a.exe",r"./FastOS-Shell.exe" )
    print("Compiling: FastOS-Bootloader")
    if os.system("g++ ./src/FastOS-Bootloader.cpp") == 0:
        print("Done!")
    else:
        print ("Error")
    os.rename(r"./a.exe",r"./FastOS-Bootloader.exe" )
    print("Finish!")
    print("Start FastOS by typing: ./FastOS-Bootloader.exe or in linux/macos ./FastOS-Bootloader")
if (Quest == "no"):
    print("Canceled")