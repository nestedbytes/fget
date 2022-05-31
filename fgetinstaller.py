import os
import urllib
import shutil
import urllib.request
import sys
def quitapp():
    sys.exit()
def uninstall():
    askun = input("Do you want to uninstall fget. y or n:")
    if askun == "y":
        print("removing fget")
        path3 = "C:/fget"
        os.remove(path3)
        print("We have removed fget from your computer ):")
    if askun == "n":
        print("Uninstall is aborted") 
def update():
    path2 = "C:/fget"
    os.remove(path2)
    install()
def reinstall():
    ask = input("Do you want to reinstall fget ? y or n:")
    if ask == "y":
        path = 'C:/fget'
        os.remove(path)
        install()
    if ask == "n":
        print("Reinstall is aborted")
def install():
    path = 'C:/fget'
    downloadurl = "https://github.com/shourgamer2/fget/releases/download/update%2Fdownload/fget.exe"
    

    print("Making fget folder")
    os.mkdir(path) 
    
    
    print("Downloading fget")
    urllib.request.urlretrieve(downloadurl,"fget.exe")
    print("Moving fget.exe to its folder")
    shutil.move("./fget.exe", "C:/fget/fget.exe")
    print("Adding fget to path")
    os.system('setx /M path "%path%;C:\fget"')

    
    
   
print("What do you want to do")
print("type 1 to install fget")
print("type 2 to reinstall fget")
print("type 3 to update fget")
print("type 4 to uninstall fget")
print("type 5 to exit")
option = input("Enter what do you want to do:")

if option == "1":
    install()
if option == "2":
    reinstall()

if option == "3":
    update()

if option == "4":
    uninstall()
if option == "5":
    quitapp()

