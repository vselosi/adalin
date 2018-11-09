from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import random
import datetime
import html5lib
import re


def getLinks(companyUrl):
    html = urlopen("http://pavtrade.com" + companyUrl)
    bsObj = BeautifulSoup(html, "html5lib")
    listOfLinks = []
    for link in bsObj.findAll("a", href = re.compile("^(/companies/)")):
        if link.attrs["href"] not in listOfLinks:
            listOfLinks.append(link.attrs["href"])
    listOfLinks = ["http://pavtrade.com" + link for link in listOfLinks]
    return listOfLinks


def getInfoBlocks(link):
    html = urlopen(link)
    bsObj = BeautifulSoup(html, "html5lib")
    print("------------------------------------------------------------------")
    print(bsObj.h1.get_text() + ":")
    try:
        infoBlocks = bsObj.find("div", {"class":"info_block bglightblue none"}).findAll("span", {"class":"dark_text"})
    except AttributeError as e:
        return None
    print("------------------------------------------------------------------")
    #infoBlocks = bsObj.findAll("span", {"class":"grey_text"}, {"class":"dark_text"})
    return infoBlocks


links = getLinks("/company/segment/distributor/production/alcohols")
for link in links:
    contacts = getInfoBlocks(link)
    print(contacts)

#<div id="companies_list">
