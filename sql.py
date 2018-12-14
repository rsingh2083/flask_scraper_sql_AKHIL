# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 23:03:27 2018

@author: Akhil
"""
import sqlite3
from flask import Flask, render_template,request,url_for
i=0
conn = sqlite3.connect('newdb.db')
print("Opened database successfully")

#conn.execute('CREATE TABLE datastream (ID INTEGER, Title TEXT, Link TEXT, texts TEXT)')
#print("Table created successfully")
conn.close()

app = Flask(__name__)
@app.route('/')
def welcome():
    return """<a href = "http://localhost:5000/sqlshow"> Show Data</a><br><a href="http://localhost:5000/enter"> Enter Data</a>"""
@app.route('/enter')
def enter():
  return render_template('SQLFETCH.html')    
@app.route('/sql',methods = ['POST', 'GET'])
def sqlinput():
    global i
    if request.method == 'POST':
      try:
         ID = i
         i=i+1
         Title = request.form['Title']
         Link = request.form['Link']
         Texts = request.form['texts']
         
         with sqlite3.connect("newdb.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO datastream (ID,Title,Link,texts) VALUES (?,?,?,?)",(ID,Title,Link,Texts))
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("results.html",msg = msg)
         con.close()
@app.route('/sqlshow')
def list():
   con = sqlite3.connect("newdb.db")
   con.row_factory = sqlite3.Row
   
   cur = con.cursor()
   cur.execute("select * from datastream")
   
   rows = cur.fetchall(); 
   return render_template("SQLSHOW.html",rows = rows)  
if __name__ == '__main__':
   app.debug = True
   app.run()
   app.run(debug = True)