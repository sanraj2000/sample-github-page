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

     
import urllib
import requests
from bs4 import BeautifulSoup
print("Helloooo")
link = "https://fr.tradingview.com/markets/cryptocurrencies/global-charts/"
#link ="https://www.wongnai.com/businesses?originalQ=sushi&mode=2&domain=1&page.number=1&cregion=8828&locale=en&categories=30&rerank=false&regions=1";
#html = requests.get(link).text
html = urllib.request.urlopen(link).read()
"""If you do not want to use requests then you can use the following code below 
   with urllib (the snippet above). It should not cause any issue."""
soup = BeautifulSoup(html, "lxml")
#res = soup.findAll("article", {"class": "listingItem"})
for title in soup.find_all("div", {"class": "tabTitle-qQlkPW5Y"}):
#for title in soup.find_all('div',class_='body'):
     print(title.text)
alpha = soup.find_all('div', attrs={'class':"sc-1d7kslo-11 cWzosZ"})

for element in alpha:
    print (element.text)  
  
  
url = "http://kite.com"
url_contents = urllib.request.urlopen(url).read()

soup = BeautifulSoup(url_contents, "html")
div = soup.find("div", {"id": "home-template"})
div2 =soup.find("div",{"class": "homepage-new__hero__download"})

content = str(div2.text)

print(content)  
  
