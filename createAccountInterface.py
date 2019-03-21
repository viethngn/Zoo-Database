#!/usr/bin/python
# -*- coding: utf-8 -*-
# filename: createAccountInterface.py
"""
Created on Sun Apr 29 14:31:35 2018

@author: RVBFM
"""

def showCreateAccount():
    print("Content-Type: text/html; charset=urf-8")    
    print()

    print("""
    <html>
        <head>
            <meta charset="utf-8">
            <title>Zoo Database Visitor Account Creating</title>
        </head>
        <body>
            <h2>Please fill in all mandatory information</h2>
            <form method="post" action="./createAccount.py" name="Visitor Information">
                First Name: <input type="text" name="fname" required><br><br>
                Last Name: <input type="text" name="lname" required><br><br>
                Address: <input type="text" name="address" required><br><br>
                City: <input type="text" name="city" required><br><br>
                State: <input type="text" name="state" required><br><br>
                Zipcode: <input type="text" name="zipcode" required><br><br>
                Birthday: <input type="date" name="birthday" required><br><br>
                Email: <input type="email" name="email" required><br><br>
                <input type="submit" value="submit">
            </form>
        </body>
    </html>      
    
    """)
if __name__ == "__main__":
    showCreateAccount()
