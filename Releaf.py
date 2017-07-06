
# coding: utf-8

# In[1]:

import pandas

from selenium import webdriver

from bs4 import BeautifulSoup

import urllib

import time
import csv
from urllib.request import urlretrieve
from PIL import Image

import os

f = open(r'G:\company.csv', 'r')

f.readline()

output = []

for line in f:
    cells = line.split(",")
    output.append((cells[0]))
f.close()
print(output)

[x.strip() for x in output if x.strip()]

chrome_path = r'C:\Users\teleworld\Desktop\chromedriver_win32\chromedriver.exe'

driver = webdriver.Chrome(chrome_path)
with open("G:\output.csv",'w') as f:
    writer = csv.writer(f,delimiter=' ',lineterminator='\n',)
    for it in output:
        driver.get("http://google.com")
        search = driver.find_element_by_id("lst-ib")
        search.send_keys(str(it))
        time.sleep(7)
        click = driver.find_element_by_class_name("sbico-c")
        click.click()
        time.sleep(7)
        driver.find_element_by_xpath('.//*[@id="rso"]/div[1]/div/div/div/div/h3/a').click()
        time.sleep(7)
        url = driver.current_url
        type(url)
        print(it, url)
        writer.writerow((it, url))
        website = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(website, "html.parser")
        
        for img in soup.findAll('img'):
            time.sleep(10)
            temp = img.get('src')
            time.sleep(10)
            a = 1
            filename = r'G:\\' + it + '\\' + str(a) + '.jpeg'
            if not os.path.exists(filename):
                os.makedirs(filename)
            a = a+1
            image = Image.open(filename)
            image.save(filename)
    driver.close()


# In[ ]:

import pandas

from selenium import webdriver

from bs4 import BeautifulSoup

import urllib

import time
import csv
from urllib.request import urlretrieve
from PIL import Image

import os

f = open(r'G:\company.csv', 'r')

f.readline()

output = []

for line in f:
    cells = line.split(",")
    output.append((cells[0]))
f.close()
print(output)

[x.strip() for x in output if x.strip()]

chrome_path = r'C:\Users\teleworld\Desktop\chromedriver_win32\chromedriver.exe'

driver = webdriver.Chrome(chrome_path)
with open("G:\output.csv",'w') as f:
    writer = csv.writer(f,delimiter=' ',lineterminator='\n',)
    for it in output:
        driver.get("http://google.com")
        search = driver.find_element_by_id("lst-ib")
        search.send_keys(str(it))
        time.sleep(7)
        click = driver.find_element_by_class_name("sbico-c")
        click.click()
        time.sleep(7)
        driver.find_element_by_xpath('.//*[@id="rso"]/div[1]/div/div/div/div/h3/a').click()
        time.sleep(7)
        url = driver.current_url
        type(url)
        print(it, url)
        writer.writerow((it, url))
        website = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(website, "html.parser")
        
        for img in soup.findAll('img'):
            time.sleep(10)
            temp = img.get('src')
            time.sleep(10)
            a = 1
            filename = r'G:\\' + it + '\\' + str(a) + '.jpeg'
            if not os.path.exists(filename):
                os.makedirs(filename)
            a = a+1
            image = Image.open(filename, "rb")
            image.save(filename)
    driver.close()

