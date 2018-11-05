from urllib.request import urlopen
from bs4 import BeautifulSoup
import html5lib

html = urlopen(input("set the url: "))
bsObj = BeautifulSoup(html, "html5lib")

for child in bsObj.find("div",{"class":"webcam"}).children:
    print(child)
