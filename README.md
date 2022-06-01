# fget
A cli used to download files from the web
# Download and setup
Download <br>
[Download](https://github.com/shourgamer2/fget/releases/download/ins/fgetinstaller.EXE) <br>
Setup <br>
Open the exe file as admin by right clicking and type 1 and hit enter to install fget ! 
# Usage
```sh
fget <urlhere> <filenamewithextensionhere>
```
Example 
```sh
fget https://github.com/shourgamer2/fget/releases/download/ver1.0.0/fget.exe fget.exe 
```
# Modify
Clone
```sh
git clone https://github.com/shourgamer2/fget
```
Cd
```sh
cd fget
```
Install all the packages
```sh
python -m pip install -r requirements.txt
```
Modify <br>
Import the packages 
```python
import typer
import urllib.request
import os
from requests import get
```
Vars
```python
latestversion = get('https://raw.githubusercontent.com/shourgamer2/fget/main/version.txt').text
version = "1.0.0"
```
Make the typer app
```python
app = typer.Typer()
```
Making the command
```python
@app.command()
def fget(geturl: str, name: str):
   if (latestversion.strip() == version):
       url = geturl
       fname = name
       cwd = os.getcwd()

       print(f"Downloading file from {url} with the name {fname}")
        
       urllib.request.urlretrieve(url,fname)
       print(f"File downloaded to {cwd}")
    
   else:
       print ("This version is outdated go to https://github.com/shourgamer2/fget and download the latest version ")
    



if __name__ == "__main__":
    app()
```
