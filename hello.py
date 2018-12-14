# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 17:19:40 2018

@author: Akhil
app.add_url_rule(functions)
flask.url_for(function,function arguments) -> goes to the url attched to the function
flask.redirect(URL) -> redirects to url
@app.route('/')
def hello_world():
    return 'H'
@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))
"""

from flask import Flask,redirect,url_for,request,render_template
app = Flask(__name__)

@app.route('/')
def new():
    return render_template('login.html')
@app.route('/result')
def result():
   dic = {'phy':50,'che':60,'maths':70}
   return render_template('result.html', result = dic)

@app.route('/success/<name>')
def success(name):
   return 'Salaam %s Bhai' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))
if __name__ == '__main__':
   app.debug = True
   app.run()
   app.run(debug = True)