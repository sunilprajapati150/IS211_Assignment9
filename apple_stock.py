#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module generates stock prices"""

import urllib2
import json
from bs4 import BeautifulSoup


url = 'http://finance.yahoo.com/quote/AAPL/history?ltr=1'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read(), "lxml")


def appleStock():
    rows = soup.find_all('tr')
    for i in rows:
        try:
            date = i.contents[0].get_text()
            close = i.contents[5].get_text()
            json_string = {"Date": date, "Close_Price": close}
            print(json.dumps(json_string))
        except:
            continue
    return


if __name__ == "__main__":
    appleStock()
