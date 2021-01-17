import json
import requests
from bs4 import BeautifulSoup
url="https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3000609"
variable=requests.get(url)
soup=BeautifulSoup(variable.text,'lxml')
lis=[]
def apple(): 
 pri=soup.find("a",{"href":"https://doi.org/10.1371/journal.pbio.3000609"}).get_text()
 print(pri) 
 for i in soup.find_all("div",{"class":"carousel-item lightbox-figure"}):
  kali=i.get('data-doi')
  k=str(kali).replace("10.1371/journal","https://doi.org/10.1371/journal")
  lis.append(k) 
  print(lis) 


#https://doi.org/10.1371/journal.pbio.3000609.g001
 return pri,lis
pri,lis=apple()
a=soup.find("h2").get_text()
print(a)
    
    
act=dict()
act['doi']=pri
act['img url']=lis
act['ALT']=a
print(act)

add=open("open.json","w")
json.dump(act,add)
add.close()

 
