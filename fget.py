import typer
import urllib.request
import os
from requests import get
latestversion = get('https://raw.githubusercontent.com/shourgamer2/fget/main/version.txt').text
version = "1.0.0"
app = typer.Typer()
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