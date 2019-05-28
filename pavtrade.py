# in[0]
import requests
from urllib.error import HTTPError
import re
import html5lib
from bs4 import BeautifulSoup
import itertools
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import pymysql

# In[1]
def getSegmentAll(startUrl):
    html = requests.get(startUrl, timeout=15)
    bsObj = BeautifulSoup(html.content, "html5lib")
    segmentAll = []
    for link in bsObj.find("div", {"id":"segment_all"}).findAll("a", {"class":"ci_link", "href":re.compile("^(/fmcg/)")}):
        if link.attrs["href"] not in segmentAll:
            segmentAll.append(startUrl+link.attrs["href"])
    return segmentAll


# In[2]
def getTitleItems(startUrl):
    html = requests.get(startUrl, timeout=15)
    bsObj = BeautifulSoup(html.content, "html5lib")
    titleItems = []
    for link in bsObj.findAll("a", {"class":"title_item", "href":re.compile("^(/fmcg/)")}):
        if link.attrs["href"] not in titleItems:
            titleItems.append(link.attrs["href"])
    return titleItems


# In[3]
def getCatItems(ci_url):
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get(ci_url)
    time.sleep(5)
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    html = driver.page_source
    assert "No results found." not in driver.page_source
    driver.close()
    bsObj = BeautifulSoup(html, "html5lib")
    ceTitles = []
    for link in bsObj.findAll("a", {"class":"c_e_title", "href":re.compile("^(/companies/)")}):
        if link.attrs["href"] not in ceTitles:
            ceTitles.append("http://pavtrade.com" + link.attrs["href"])
    return ceTitles


# In[4]
def getInfoBlocks(ceTitle):
    html = requests.get(ceTitle, timeout=15)
    bsObj = BeautifulSoup(html.content, "html5lib")
    darkText = []
    try:
        print(bsObj.h1.get_text() + "| ")
        info_block = bsObj.find("div", {"class":"info_block bglightblue none"})
        for link in info_block.findAll("span", {"class":re.compile("^(dark_text)")}):
            darkText.append(link.get_text())
    except:
        if AttributeError or TypeError:
            None
    darkText = "| ".join(darkText)
    return darkText


# In[5]
def mysqlInteraction(dbName, tableName, columnName, infoBlock):
    conn = pymysql.connect(host = "127.0.0.1", unix_socket = "/run/mysqld/mysqld.sock", user = "root", passwd = None, db = "mysql", charset = "utf8")
    cur = conn.cursor()

    try:
        cur.execute(f"CREATE DATABASE IF NOT EXISTS {dbName};")
        cur.execute(f"USE {dbName};")
        cur.execute(f"CREATE TABLE IF NOT EXISTS {tableName} (id BIGINT (7) NOT NULL AUTO_INCREMENT PRIMARY KEY, {columnName} TEXT (3000) DEFAULT NULL);")
        cur.execute(f"ALTER TABLE {tableName} ADD COLUMN IF NOT EXISTS {columnName} TEXT (3000) DEFAULT NULL;")
        cur.execute(f"INSERT INTO {tableName} ({columnName}) VALUES ('{infoBlock}');")
    except pymysql.err.ProgrammingError:
        #cur.execute(f"INSERT INTO {tableName} ({columnName}) VALUES ('{infoBlock}');")
        cur.execute(f'INSERT INTO {tableName} ({columnName}) VALUES ("{infoBlock}");')
    finally:
        conn.commit()
        cur.close()
        conn.close()


def ciLinks(startUrl):
    titleItems = getTitleItems(startUrl)
    cycleTitleItems = itertools.cycle(titleItems)
    for i in range(len(titleItems)):
        segmentAll = getSegmentAll(startUrl)
        titleItem = next(cycleTitleItems)
        titleSegments = [i.replace("/fmcg", titleItem) for i in segmentAll]
        for ci_url in titleSegments:
            ceTitles = getCatItems(ci_url)
            dbName = ci_url.split("/fmcg/")[0]
            dbName = dbName.replace("http://pavtrade.com", "pavtrade")
            ci_url = ci_url.split("/fmcg/")[1]
            tableName = ci_url.split("/")[0].replace("-", "_")
            columnName = ci_url.split("/")[1].replace("-", "_")
            for ceTitle in ceTitles:
                infoBlocks = getInfoBlocks(ceTitle)
                for infoBlock in infoBlocks:
                    print(infoBlock)
                    mysqlInteraction(dbName, tableName, columnName, infoBlock)

#cur.execute(f"UPDATE {tableName} SET {columnName}='{infoBlock}';")
ciLinks("http://pavtrade.com")
