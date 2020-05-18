# Web Scraper for Deal Sourcing
I built a web scraper to source businesses' contact information for [Studio 50-50](https://studio50-50.com/)'s marketing outreach. Contacts are scraped from the web and stored in an Excel sheet. This program was built using Python, BeautifulSoup, requests, and Chrome Dev Tools.

## How It Works
When you run the code for web scraping, a request is sent to the URL that you have mentioned. As a response to the request, the server sends the data and allows you to read the HTML or XML page. The code then, parses the HTML or XML page, finds the data and extracts it.

To extract data using web scraping with python, you need to follow these basic steps:
1. Find the URL that you want to scrape
2. Inspecting the Page
3. Find the data you want to extract
4. Write the code
5. Run the code and extract the data
6. Store the data in the required format

## Tools and Tech
- **BeautifulSoup**: Beautiful Soup is a Python package for parsing HTML and XML documents. It creates parse trees that is helpful to extract the data easily.
- **Pandas**: Pandas is a library used for data manipulation and analysis. It is used to extract the data and store it in the desired format.
- **Requests**: The requests module allows you to send HTTP requests using Python. The HTTP request returns a Response Object with all the response data (content, encoding, status, etc).

## Real Estate Websites
- https://www.point2homes.com/CA/Real-Estate-Agents/ON/Ottawa.html
- https://business.ottawabot.ca/list/ql/re-construction-development-12
- https://www.oreb.ca/find-a-realtor/residential-result/

## Useful Resources
- https://www.youtube.com/watch?v=ng2o98k983k
- https://realpython.com/beautiful-soup-web-scraper-python/#part-1-inspect-your-data-source
- https://www.edureka.co/blog/web-scraping-with-python/
- https://www.dataquest.io/blog/web-scraping-tutorial-python/
- Difference Between Parsers: https://goo.gl/zdy9br
- Python File Objects: https://youtu.be/Uh2ebFW8OYM
- Python Strings: https://youtu.be/k9TUPpGqYTo
- Python Try/Except: https://youtu.be/NIWwJbo-9_8
- Python CSV Files: https://youtu.be/q5uM4VKywbA