import requests
import wget
from zipfile import ZipFile
import os

def download():
    dl="https://chromedriver.storage.googleapis.com/"
    driver="https://chromedriver.chromium.org/downloads"
    check="https://www.filecroco.com/download-chrome/"
    file="chromedriver_win32.zip"

    content=requests.get(check)
    cver=''.join(content.text).split("\n")[11]
    cver=cver.split("Latest version:")[1][37:39]
    content=requests.get(driver)
    dver=''.join(content.text).split("\n")[127]
    dver=dver.split("If you are using Chrome version "+str(cver))[1][94:]
    dver=dver.split("/")[0]
    wget.download(dl+str(dver)+"/chromedriver_win32.zip")
    with ZipFile(file, 'r') as zip:
        zip.extractall()
    os.remove("./chromedriver_win32.zip")
download()
