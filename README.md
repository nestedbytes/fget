# fget
A cli used to download files from the web
# Download and setup
Download <br>
[Download](https://github.com/shourgamer2/fget/releases/download/ver1.0.0/fget.exe) <br>
Setup <br>
First of all make a folder in your C: drive called "fget" and move the exe which you download there
![image](https://user-images.githubusercontent.com/90188229/169689803-dbb958cf-a8e9-40f4-b896-be99cbef6298.png) <br>
Then search for "edit the system environment variables" in your start <br>
![image](https://user-images.githubusercontent.com/90188229/169689847-f579b2c9-403c-477c-91dd-82c2d830a86d.png) <br>
Open it then open Enviroment Variables from there <br>
![image](https://user-images.githubusercontent.com/90188229/169689888-732128f7-3cbe-4a34-b4ec-34c1e7bfe93e.png) <br>
Select path and click Edit <br>
![image](https://user-images.githubusercontent.com/90188229/169689944-7ca10e62-dae3-4e74-b5e9-a04c8367e4dd.png) <br>
Then click on the white space to deselect anything which was selected. And click on browse <br>
![image](https://user-images.githubusercontent.com/90188229/169689991-4508d606-7eca-43ed-b690-0ed345e1685b.png) <br>
From here open this pc.Then select your c drive then select the fget folder you made and click ok <br>
![image](https://user-images.githubusercontent.com/90188229/169690039-f8633460-c2a8-4ab5-bf36-14abef232435.png) <br>
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
