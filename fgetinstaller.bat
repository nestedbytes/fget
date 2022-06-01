@echo off
title Fget-Installer
echo Fget-Installer
echo Version 1.0.0
echo Press 1 to install Fget
echo press 2 to Reinstall Fget
echo Press 3 to Update Fget
echo Press 4 to Uninstall Fget
echo press 5 to Exit
set /p car=
if %car% == 1 goto install
if %car% == 2 goto reinstall
if %car% == 3 goto update
if %car% == 4 goto uninstall
if %car% == 5 goto exit
:install
echo making the fget folder 
mkdir C:\fget
echo downloading the file
powershell Invoke-WebRequest https://github.com/shourgamer2/fget/releases/download/download/fget.exe -OutFile c:\fget\fget.exe
setx /M path "%path%;C:\fget"
pause
:reinstall
echo reinstalling
echo removing old folder
rmdir /s C:\fget\
echo making new folder
mkdir C:\fget
echo downloading file
powershell Invoke-WebRequest https://github.com/shourgamer2/fget/releases/download/download/fget.exe -OutFile c:\fget\fget.exe
setx /M path "%path%;C:\fget"
exit
:update
echo updating
echo removing old folder
rmdir /s C:\fget\
echo making new folder
mkdir C:\fget
echo downloading file
powershell Invoke-WebRequest https://github.com/shourgamer2/fget/releases/download/download/fget.exe -OutFile c:\fget\fget.exe
setx /M path "%path%;C:\fget"
exit
:uninstall
echo uninstalling 
rmdir /s C:\fget\
exit
:exit
exit
