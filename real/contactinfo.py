# https://business.ottawabot.ca/list/

# *** IMPORT LIBRARIES ***
from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
import numpy as np
from selenium import webdriver

# *** OPEN FILE FROM WEB USING REQUEST ***
source = requests.get('https://business.ottawabot.ca/list/ql/re-construction-development-12').text
soup = BeautifulSoup(source, 'lxml')

# *** CSV FILE ***
csv_file = open('contactinfo.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Name', 'Company', 'Website', 'Email', 'Phone', 'Address'])


# *** CONTACT BLOCK ***
containers = soup.find('div', {'class': 'gz-list-card-wrapper col-sm-6 col-md-4'})
# print(len(containers)) - prints number of contacts
# print(containers.prettify()) - prints formated html

# COMPANY
companyblock = containers.find('div',{'class': 'card-header'})   # print(nameblock.prettify())
company = companyblock.find('a')['alt']
print(company)

# ADDRESS
addressphoneblock = containers.find('div', {'class': 'card-body gz-results-card-body'})
address = addressphoneblock.find('span', {'class': 'gz-street-address'}).getText()
print(address)

# PHONE NUMBER
phoneblock = addressphoneblock.find('li', {'class': 'list-group-item gz-card-phone'})
p = phoneblock.find('a', 'card-link')['href']
phone = p.replace('tel:', '')
print(phone)

# EMAIL

# WEBSITE

# NAME

"""
for contactblock in entireblock.find_all('listing-grid'):
# contactblock = entireblock.find('div', 'listing-grid')
    # *** SOURCE INFO ***
    # TOP - name and phone
    top = contactblock.find('div', 'top')
    name = top.find('div', 'top-box').h5.text
"""