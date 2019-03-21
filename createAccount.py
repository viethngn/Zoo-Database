#!/usr/bin/python
print("Content-Type: text/html")
print() 
# -*- coding: utf-8 -*-

import cgi
import cgitb; cgitb.enable()

from projectzoodb import projectzooDB


# Create a database object that will handle all the DB stuff.
dbobj = projectzooDB()

def createNewVisitor():
    form = cgi.FieldStorage()

    fname = form["fname"].value 
    lname = form["lname"].value
    address = form["address"].value
    city = form["city"].value
    state = form["state"].value
    zipc = form["zipcode"].value
    bday = form["birthday"].value
    email = form["email"].value
    dbobj.createNewVisitorAccount(fname,lname, address, city, state, zipc, bday, email)
    
def doHTMLHead():

    print("""
    <html>
    <head>
    <title>Create Account</title>
    </head>
    <body>
    """)
def doHTMLTail():

    print("""
    </body>
    </html>

    """)

if __name__ == "__main__":
    createNewVisitor()
    doHTMLHead()
    print("""<p>Account created</p>""")
    print("""<a href="./login.html">Go to back to log in page</a>""")
    doHTMLTail()




