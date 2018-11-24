from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import random
import datetime
import html5lib
import re
import pymysql

random.seed(datetime.datetime.now())

conn = pymysql.connect(host = "127.0.0.1", user = "root", passwd = None, unix_socket = "/run/mysqld/mysqld.sock", db = "mysql", charset = "utf8" )
cur = conn.cursor()
cur.execute("USE scraping")

def getBasicLinks(basicLink):
    html = urlopen(basicLink)
    bsObj = BeautifulSoup(html, "html5lib")
    listOfBasicLinks = []
    for link in bsObj.findAll("a", href = re.compile("^(/fmcg/)")):
        if link.attrs["href"] not in listOfBasicLinks:
            listOfBasicLinks.append(link.attrs["href"])
    listOfBasicLinks = [basicLink + link for link in listOfBasicLinks]
    return listOfBasicLinks

def getLinks(basicLink):
    html = urlopen(basicLink)
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
    #title = bsObj.h1.get_text() + ":"
    try:
        infoBlocks = bsObj.find("div", {"class":"info_block bglightblue none"}).findAll("span", {"class":"dark_text"})

        #content = infoBlocks
        for link in infoBlocks:
            print(link.string)
    except AttributeError as e:
        return None
    print("------------------------------------------------------------------")
    #infoBlocks = bsObj.findAll("span", {"class":"grey_text"}, {"class":"dark_text"})
    #cur.execute("INSERT INTO pages (title, content) VALUES (\"%s\", \"%s\")", (title, content))
    #cur.connection.commit()
    return infoBlocks


basicLinks = getBasicLinks("http://pavtrade.com")
try:
    while  len(basicLinks) > 0:
        for basicLink in basicLinks:
            links = getLinks(basicLink)
            for link in links:
                getInfoBlocks(link)
                #contacts = getInfoBlocks(link)
                #print(contacts)

        newBasicLinks = basicLinks[random.randint(0, len(basicLinks)-1)].attrs["href"]
        print(newBasicLinks)
        basicLinks = getBasicLinks(newBasicLinks)
finally:
    cur.close()
    conn.close()

#<div id="companies_list">
