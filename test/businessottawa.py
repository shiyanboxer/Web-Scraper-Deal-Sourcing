# https://business.ottawabot.ca/list/

# *** IMPORT LIBRARIES ***
from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
from selenium import webdriver


# *** OPEN FILE FROM WEB USING REQUEST ***
source = requests.get('https://business.ottawabot.ca/list/ql/re-construction-development-12').text
soup = BeautifulSoup(source, 'lxml')


# *** CSV FILE ***
csv_file = open('businessottawa.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Company', 'Address', 'Phone'])


# *** CONTACT BLOCK ***
containers = soup.find('div', {'class': 'gz-list-card-wrapper col-sm-6 col-md-4'})

for container in containers:
 
    # print(len(containers)) - prints number of contacts
    # print(containers.prettify()) - prints formated html

    # COMPANY
    companyblock = containers.find('div',{'class': 'card-header'})
    company = companyblock.find('a')['alt']
    # print(company)
     
    # ADDRESS
    addressphoneblock = containers.find('div', {'class': 'card-body gz-results-card-body'})
    address = addressphoneblock.find('span', {'class': 'gz-street-address'}).getText()
    # print(address)

    # PHONE NUMBER
    phoneblock = addressphoneblock.find('li', {'class': 'list-group-item gz-card-phone'})
    p = phoneblock.find('a', 'card-link')['href']
    phone = p.replace('tel:', '')
    # print(phone)
    
    
    # *** WRITE AND CLOSE CSV ***
    # write the data to CSV for every iteration
    csv_writer.writerow([company, address, phone])

# outside of the loop, close the file
csv_file.close()