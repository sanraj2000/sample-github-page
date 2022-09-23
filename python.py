from bs4 import BeautifulSoup
markup = '''<html><body><div id="container">Div Content</div></body></html>''
soup = BeautifulSoup(markup, 'html.parser')
div_bs4 = soup.find('div', id = "container")
print(div_bs4.string)
