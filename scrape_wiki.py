from urllib.request import urlopen
from bs4 import BeautifulSoup
import html5lib
import re
import datetime
import random
'''
html = urlopen(input("sat the url: "))
bsObj = BeautifulSoup(html, "html5lib")
for link in bsObj.findAll("a"):
    if "href" in link.attrs:
        print(link.attrs["href"])
'''

html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html, "html5lib")
for link in bsObj.find("div", {"id":"bodyContent"}).findAll("a", href = re.compile("^(/wiki/)((?!:).)*$")):
    if "href" in link.attrs:
        print(link.attrs["href"])
'''

random.seed(datetime.datetime.now())

def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html, "html5lib")
    #return bsObj.find("div", {"id":"bodyContent"}).findAll("a", href = re.compile("^(/wiki/)(?!:).*$"))
    return bsObj.findAll("a", href = re.compile("^(/wiki/)(?!:).*$"))

links = getLinks("/wiki/Kevin_Bacon")
while len(links) > 0:
        newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
        print(newArticle)
        links = getLinks(newArticle)
'''
