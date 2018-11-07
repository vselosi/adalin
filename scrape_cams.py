from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import datetime
import random
import re
import html5lib


random.seed(datetime.datetime.now())

def getLinks(camUrl):
    try:
        html = urlopen("http://webcam.scs.com.ua/europe"+camUrl)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html, "html5lib")
    except AttributeError as e:
        return None
    return bsObj.find("div", {"class":"webcam"}).findAll("a", {"href":re.compile("(/ukraine/)")})
    #return bsObj.find("div", {"class":"webcam"})

#links = getLinks("/ukraine/lviv/tsentr-lvova-prospekt-svobody/")

links = getLinks("/ukraine/lviv/tsentr-lvova-prospekt-svobody/")
while  len(links) > 0:
    newCam = links[random.randint(0, len(links)-1)].attrs["href"]
if links == None:
    print("There is something wrong!")
else:
    print(newCam)
    links = getLinks(newCam)
