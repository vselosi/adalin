from urllib.request import urlopen
from bs4 import BeautifulSoup
import html5lib

html = urlopen(input("set the url: "))
bsObj = BeautifulSoup(html, "html5lib")
print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())
