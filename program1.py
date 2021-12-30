# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 09:52:38 2021

@author: Zulfiqar
"""

import requests
from bs4 import BeautifulSoup

url = 'https://sis.cuiatd.edu.pk/'

page = requests.get(url)


soup = BeautifulSoup(page.text,'lxml')
#print (soup)
print(soup.body.font.string)

import scrapy