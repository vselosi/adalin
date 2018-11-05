from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import datetime
import random
import re
import html5lib


random.seed(datetime.datetime.now())

def getLinks(camUrl):

    html = urlopen("http://webcam.scs.com.ua/europe"+camUrl)
    bsObj = BeautifulSoup(html, "html5lib")
    return bsObj.findAll("a", {"href":re.compile("(/ukraine/)(?!:).*$")})
    #return bsObj.find("div", {"class":"webcam"})

#links = getLinks("/ukraine/lviv/tsentr-lvova-prospekt-svobody/")
def linksError():
    links = getLinks("/ukraine/lviv/tsentr-lvova-prospekt-svobody/")
    lnk = links
    try:
        while  len(links) > 0:
            newCam = links[random.randint(0, len(links)-1)].attrs["href"]
            print(newCam)
            links = getLinks(newCam)
    except HTTPError as e:
        #links = getLinks("/ukraine/lviv/tsentr-lvova-prospekt-svobody/")
        #return lnk
#lk = linksError()
#print(lk)

        while  len(links) > 0:
            newCam = links[random.randint(0, len(links)-1)].attrs["href"]
            print(newCam)
            links = getLinks(newCam)
