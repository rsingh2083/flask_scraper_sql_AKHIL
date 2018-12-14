link="https://www.bing.com/search?q=halli labs"

import requests
import json
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36'}

from selenium import webdriver
#browser=webdriver.Firefox()
#link=("https://www.google.co.in/search?safe=off&rlz=1C1CHBF_enIN807IN807&ei=q1_AW_jAC4bMvwTe0ofgDw&q=has+acquired&oq=has+acquired&gs_l=psy-ab.3..0i67k1l2j0i22i30k1l8.3065.3191.0.3390.2.2.0.0.0.0.144.144.0j1.1.0....0...1.1.64.psy-ab..1.1.144....0.evCY9V6Np8Y")
#browser.get(link)
s=requests.get(link, headers=headers)
soup =BeautifulSoup(s.content,'html.parser')

mill_google=[]
for i in soup.findAll("li", {"class": "b_algo"}):
    #print (i.getText())
    temp=[]
    for j in i.findAll("h2"):
        title=(j.text)
        temp.append(title)
        #print (i.findAll("h3")[0].text)
        #print ("*******************************")
    for k in i.findAll("h2"):
        link= j.contents[0]['href']
        temp.append(link)
        #print ("*******************************")
    for l in i.findAll("p"):
        summary= (l.getText())
        temp.append(summary)
        #print ("*******************************")
    #temp.append(i.findAll("h3")[0].text)
    mill_google.append(temp)