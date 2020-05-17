# *** IMPORT LIBRARIES ***
from bs4 import BeautifulSoup
import requests
import csv

# *** OPEN FILE FROM WEB USING REQUEST ***
source = requests.get('https://www.oreb.ca/find-a-realtor/residential-result/').text
soup = BeautifulSoup(source, 'lxml')

# *** CSV FILE ***
csv_file = open('oreb.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Name', 'Company', 'Website', 'Email', 'Phone', 'Address'])

# *** SOURCE INFO ***
""" 
for loop that iterates over all articles in the page
article in this case contains the heading, description, and video link
use for loop and find_all method to iterate get all articles content in the page
"""
for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)
    
    # find method finds searches for a  div of specific class
    # by adding p.text we get the content, if we didn't we would get the html
    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    # geting the link, the link is in an iframe under source
    try:
        # returns video link
        vid_src = article.find('iframe', class_='youtube-player')['src'] # access source attribute

        # use the split method to split the url based on values
        vid_id = vid_src.split('/')[4] # get the 4th index
        vid_id = vid_id.split('?')[0]

        # f string to format the string
        yt_link = f'https://youtube.com/watch?v={vid_id}'
    
    # *** ERROR MANAGEMENT ***
    # in case there is missing content, use try except block 
    except Exception as e:
        # copy paste everything in the youtube link block
        yt_link = None # could not get youtube link so set to none
    print(yt_link) 
    print() # black line

    # *** WRITE AND CLOSE CSV ***
    # write the data to CSV for every iteration
    csv_writer.writerow([headline, summary, yt_link])

# outside of the loop, close the file
csv_file.close()
