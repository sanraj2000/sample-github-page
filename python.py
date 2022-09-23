#from bs4 import BeautifulSoup
#markup = '''<html><body><div id="container">Div Content</div></body></html>'''
#soup = BeautifulSoup(markup, 'html.parser')
#div_bs4 = soup.find('div', id = "container")
#print(div_bs4.string)


import urllib
#from selenium import webdriver
#driver = webdriver.Chrome(/path/ToChromeWebDriver)
url = "https://fr.tradingview.com/markets/cryptocurrencies/global-charts/"
#driver.get(url)
html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html, 'html.parser')
for title in soup.find_all("div", {"class": "tabTitle-qQlkPW5Y"}):
     print(title.string)
