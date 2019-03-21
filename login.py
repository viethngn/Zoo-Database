#!/usr/bin/python

print("Content-Type: text/html")
print()

import cgi
import cgitb; cgitb.enable()
from projectzoodb import projectzooDB
import visitor, employy, admin

dbobj = projectzooDB()


def main():
    form = cgi.FieldStorage()
    user = form["username"].value
    password = form["password"].value
    result = dbobj.checkAccountType(user, password)
    if 0 in result:
	visitor.main()
    elif 1 in result:
	employee.main()
    elif 2 in result:
	admin.main()
    else:
	print("""Account doesn't exsit""")

# Only run the main method if this was the script that was run
if __name__ == "__main__":
    main()
