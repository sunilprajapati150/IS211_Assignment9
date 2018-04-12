#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module generates stock prices"""

import urllib2
import json
from bs4 import BeautifulSoup

url = 'https://www.wunderground.com/history/airport/KNYC/2015/1/11/MonthlyHistory.html'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read(), "lxml")


def getWeather():
    rows = soup.find_all('tr')
    rownum = 0
    for i in rows:
        if rownum < 11:
            try:
                date = i.contents[0].get_text()
                temp = i.contents[1].get_text()
                json_string = {"Date": date, "Temp": temp}
                print(json.dumps(json_string))
                rownum += 1
            except:
                continue
        else:
            for i in rows:
                try:
                    date = i.contents[0].get_text()
                    temp = i.contents[2].get_text()
                    json_string = {"Date": date, "Temp": temp}
                    print(json.dumps(json_string))
                    rownum += 1
                except:
                    continue
    return


if __name__ == "__main__":
    getWeather()
