# https://business.ottawabot.ca/list/ql/re-construction-development-12

# *** IMPORT LIBRARIES ***
from bs4 import BeautifulSoup
import requests
import csv
import pandas

# *** OPEN FILE FROM WEB USING REQUEST ***
source = requests.get('https://business.ottawabot.ca/list/ql/re-construction-development-12').text
soup = BeautifulSoup(source, 'lxml')

# *** CSV FILE ***
csv_file = open('realestate.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Name', 'Company', 'Website', 'Email', 'Phone', 'Address'])

# *** ENTER THE ENTIRE BLOCK ***
entireblock = soup.find('div', 'row gz-cards gz-results-cards')
innerblock = entireblock.find('div', class_='gz-list-card-wrapper col-sm-6 col-md-4')
for contactblock in entireblock.find_all('listing-grid'):
# contactblock = entireblock.find('div', 'listing-grid')
    # *** SOURCE INFO ***
    # TOP - name and phone
    top = contactblock.find('div', 'top')
    name = top.find('div', 'top-box').h5.text

