"""
The code from this video can be found at:
https://github.com/CoreyMSchafer/code...

Difference Between Parsers: https://goo.gl/zdy9br
Python File Objects: https://youtu.be/Uh2ebFW8OYM
Python Strings: https://youtu.be/k9TUPpGqYTo
Python Try/Except: https://youtu.be/NIWwJbo-9_8
Python CSV Files: https://youtu.be/q5uM4VKywbA
"""

# import libraries
from bs4 import BeautifulSoup
import requests
import csv

"""
OPEN HTML FILE - read in and pass in html file using lxml parser
    with open('sample.html') as html_file: 
        # soup variable which is a BeautifulSoup object of our parsed html
        soup = BeautifulSoup(html_file, 'lxml') 

        # EXAMPLE OF RETRIEVING TEXT
        article = soup.find('div', class_='article')
        headline = article.h2.a.text
        summary = article.p.text

        # PRINT ENTIRE FORMATED HTML PAGE
        print(soup.prettify())
"""

# OPEN FILE FROM WEB USING REQUEST
# this will return a response object, and with the .text it will return an html equivalent 
source = requests.get('http://coreyms.com').text

# soup variable which is a BeautifulSoup object of our parsed html
soup = BeautifulSoup(source, 'lxml')

# CSV FILE
# create a file and 'w', write to it
csv_file = open('test.csv', 'w')
# create an object, csv_writter
csv_writer = csv.writer(csv_file)
# use writerow method to write row and pass in headers 
csv_writer.writerow(['headline', 'summary', 'video_link'])

# for loop that iterates over all articles in the page
# article in this case contains the heading, description, and video link
# use for loop and find_all method to iterate get all articles content in the page
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
    
    # ERROR MANAGEMENT - in case there is missing content
    # use try except block 
    except Exception as e:
        # copy paste everything in the youtube link block
        yt_link = None # could not get youtube link so set to none
    print(yt_link) 
    print() # black line

    # write the data to CSV for every iteration
    csv_writer.writerow([headline, summary, yt_link])

# outside of the loop, close the file
csv_file.close()
