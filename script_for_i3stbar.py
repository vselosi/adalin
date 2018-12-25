#!/usr/bin/env python
from urllib.error import URLError
from urllib.request import urlopen
import json
import time
import os

os.system("setxkbmap -layout us,ru && setxkbmap -option 'grp:alt_shift_toggle'")
def getWeather():
    try:
        response = urlopen("https://api.openweathermap.org/data/2.5/find?q=Dnipro,ua&units=metric&appid=APITOKEN").read().decode('utf-8')
    except URLError:
        return print("Connection failed!")
    responseJson = json.loads(response)
    list = responseJson.get("list")
    list = list[0]
    weather = list.get("weather")
    weather = weather[0]
    output = list.get("name")+"| "+str(list.get("main").get("temp"))+" °C| "+"wind: "+str(list.get("wind").get("speed"))+" m/s| "+weather.get("description")+"| "+"cloudiness: "+str(list.get("clouds").get("all"))+"%| "+str(list.get("main").get("pressure"))+" hpa"
    return output

def getCourse():
    try:
        response = urlopen("http://bank-ua.com/export/exchange_rate_cash.json").read().decode('utf-8')
    except URLError:
        return print("Connectio failed!")
    responseJson = json.loads(response)
    list = responseJson[3]
    output = list.get("codeAlpha")+": "+list.get("rateBuy")+"/"+list.get("rateSale")+"|"
    return output

while True:
 print(getCourse(), getWeather())
 time.sleep(60)
