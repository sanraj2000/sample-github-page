import urllib
import requests
from bs4 import BeautifulSoup
url = "https://vmapigwjenkins:8443/view/APIGW%20Cloud/job/YAIC-AZURE-SPRO-1011-SPLIT-RUN/"
r = requests.get(url)
print(r.content)
#url_contents = urllib.request.urlopen(url).read()

#soup = BeautifulSoup(url_contents, "html")
#div = soup.find("div", {"id": "home-template"})
#div2 =soup.find("div",{"class": "build-icon"})
#div3= soup.find("div", {"class": "download-button__text-elements"})
#con = str(div)
#content = str(div2.text)
#content2 = str(div3.text)


#print(con[:50])
#print(con)

#print("only the div class")
#print(content)
#print("sandy sandy sandy")
#print(content2)
