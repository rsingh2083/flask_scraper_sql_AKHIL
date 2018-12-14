# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 22:41:44 2018

@author: Akhil
"""
print(__name__)
username = "Akhil"
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Search Page"

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User ' + username

if __name__ == "__main__":
    app.run()

