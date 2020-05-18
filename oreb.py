# https://www.oreb.ca/find-a-realtor/residential-result/

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
csv_file = open('real.csv', 'w')
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
    phone = top.find('div', 'bottom-box').h5.text
    print(name)
    print(phone)

    # MIDDLE - address, company, website, email
    # MIDDLE LEFT
    middle = contactblock.find('div', class_='middle')
    middleleft = middle.find('div', class_='left')
    company = middleleft.find('div', class_='h5')
    address = middleleft.find('div', class_='h6')
    print(company)
    print(address)

    # MIDDLE RIGHT - email and website links
    middleright = middle.find('div', class_='right')

    try:
        website = middleright.a['href']

    except Exception as e:
        website = None

    try:
        email = middleright.a['href']
    except Exception as e:
        email = None

    print(website)
    print(email)
    print()

    # *** WRITE CSV ***
    csv_writer.writerow[name, company, website, email, phone, address]

# *** CLOSE CSV ***
# csv_file.close()