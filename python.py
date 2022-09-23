#from bs4 import BeautifulSoup
#markup = '''<html><body><div id="container">Div Content</div></body></html>'''
#soup = BeautifulSoup(markup, 'html.parser')
#div_bs4 = soup.find('div', id = "container")
#print(div_bs4.string)


#import urllib
#import requests
#from selenium import webdriver
#driver = webdriver.Chrome(/path/ToChromeWebDriver)
#url = "https://fr.tradingview.com/markets/cryptocurrencies/global-charts/"
#driver.get(url)
#html = urllib.request.urlopen(url).read()

#soup = BeautifulSoup(html, 'html.parser')
#for title in soup.find_all("div", {"class": "tabTitle-qQlkPW5Y"}):
 #    print(title.string)

     
  

import requests
from bs4 import BeautifulSoup

link = "https://www.architecture.com/FindAnArchitect/FAAPractices.aspx?display=50"

html = requests.get(link).text

"""If you do not want to use requests then you can use the following code below 
   with urllib (the snippet above). It should not cause any issue."""
soup = BeautifulSoup(html, "lxml")
res = soup.findAll("article", {"class": "listingItem"})
for r in res:
    print("Company Name: " + r.find('a').text)
    print("Address: " + r.find("div", {'class': 'address'}).text)
    print("Website: " + r.find_all("div", {'class': 'pageMeta-item'})[3].text)
