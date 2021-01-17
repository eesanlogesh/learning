import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json



def scrap(url):

 variable=requests.get(url)
 soup=BeautifulSoup(variable.text,'lxml')
 add=soup.find("title").get_text()
 string="Chromothripsis drives the evolution of gene amplification in cancer | Nature"
 x=string.replace(" | Nature","")
 add3=soup.find("div",{"id":"Abs1-content"}).get_text()
 
 for i in soup.find_all("span", {"class" : "c-bibliographic-information__value"}):
  try:
   doi = i.find('a')['href']
  except:
   pass
   
   a=soup.find(datetime="2018-12-16").text
   date=datetime.strptime(a,'%d %B %Y').strftime('%Y %m %d')
   
 return x, add3, doi, date
 
x, add3, i, date = scrap(url="https://www.nature.com/articles/s41586-020-03064-z")
love=dict()
love['title'] = x
love['abstract'] = add3
love['doi'] = i
love['receive'] = date
print(love)
task3 = open("open.json","w")
json.dump(love,task3)
task3.close()
