# https://business.ottawabot.ca/list/ql/re-construction-development-12

# *** IMPORT LIBRARIES ***
from bs4 import BeautifulSoup
import requests
import csv
import pandas
import selenium

# *** OPEN FILE FROM WEB USING REQUEST ***
source = requests.get('https://www.oreb.ca/find-a-realtor/residential-result/').text
soup = BeautifulSoup(source, 'lxml')

# *** CSV FILE ***
csv_file = open('realestate.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Name', 'Company', 'Website', 'Email', 'Phone', 'Address'])

# *** ENTER THE ENTIRE BLOCK ***
entireblock = soup.find('div', 'listing-section')

for contactblock in entireblock.find_all('listing-grid'):
# contactblock = entireblock.find('div', 'listing-grid')
    # *** SOURCE INFO ***
    # TOP - name and phone
    top = contactblock.find('div', 'top')
    name = top.find('div', 'top-box').h5.text

