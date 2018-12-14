# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 20:47:42 2018

@author: Akhil
"""
import sqlite3
import urllib
import requests
import json
from bs4 import BeautifulSoup
from flask import Flask, render_template,request,url_for
app = Flask(__name__)
conn = sqlite3.connect('newdb.db')
conn.execute('create table if not exists datastream (ID INTEGER, Title TEXT, Link TEXT, texts TEXT)')
num = conn.cursor()
num.execute('Select * from datastream')
nums= num.fetchall()
ID = len(nums) + 1
conn.close()

@app.route('/')
def welcome():
    return render_template('Scraper_Home.html',nameoftheproject = 'Profiling Engine')
#connect to the database
@app.route('/scrape',methods = ['POST', 'GET'])
def scrape():
    if request.method == 'POST':
        try:
            CompanyName = urllib.parse.quote(request.form['Companyname'])
        except:
            print("Error!!")
    else:
        CompanyName = urllib.parse.quote(request.args.get('Companyname'))
    link = "https://www.bing.com/search?q=" + CompanyName
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36'}
    s = requests.get(link, headers=headers)
    soup = BeautifulSoup(s.content,'html.parser')
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
    return mill_google[0][1] + mill_google[0][0] + mill_google[0][2]
	
if __name__ == '__main__':
   app.debug = True
   app.run()
   app.run(debug = True)
