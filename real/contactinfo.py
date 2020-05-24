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
soup.title
# <title>Returns title tags and the content between the tags</title>
soup.title.string
# u'Returns the content inside a title tag as a string'
soup.p
# <p class="title"><b>This returns everything inside the paragraph tag</b></p>
soup.p['class']
# u'className' (this returns the class name of the element)
soup.a
# <a class="link" href="http://example.com/example" id="link1">This would return the first matching anchor tag</a>
// Or, we could use the find all, and return all the matching anchor tags
soup.find_all('a')
# [<a class="link" href="http://example.com/example1" id="link1">link2</a>,
#  <a class="link" href="http://example.com/example2" id="link2">like3</a>,
#  <a class="link" href="http://example.com/example3" id="link3">Link1</a>]
soup.find(id="link3")
# <a class="link" href="http://example.com/example3" id="link3">This returns just the matching element by ID</a>



for contactblock in entireblock.find_all('listing-grid'):
# contactblock = entireblock.find('div', 'listing-grid')
    # *** SOURCE INFO ***
    # TOP - name and phone
    top = contactblock.find('div', 'top')
    name = top.find('div', 'top-box').h5.text
"""