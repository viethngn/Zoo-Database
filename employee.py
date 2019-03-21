#!/usr/bin/python
#print("Content-Type: text/html")
#print(" ")
# -*- coding: utf-8 -*-
import time
import cgi
import cgitb; cgitb.enable()
import dbinterface

################################################################################
def doHTMLHead():

	print("""
	<html>
	<head>
	<title>employee</title>
	</head>
	<body>
	""")


################################################################################
def doHTMLTail():

	print("""
	<p>
	<hr>
	This page was generated at %s.
	</body>
	</html>

	""" % time.ctime())


################################################################################
if __name__ == "__main__":

	print("Content-Type: text/html; charset=utf-8")
	print("Cache-Control: no-cache, must-revalidate") # HTTP/1.1 
	print("Expires: Sat, 26 Jul 1997 05:00:00 GMT") # Date in the past 
	print()

	form = cgi.FieldStorage()
    
	doHTMLHead()

	#print("<br><br>")
	#print("Debugging mode with 'print form':<br>")
	#print(form)
	#print("<br><br>")

	if "updateEmployeeInfo" in form and "Gender" in form:
		FirstName = form["FirstName"].value
		LastName = form["LastName"].value
		Gender = form["Gender"].value
		Address = form["Address"].value
		City = form["City"].value
		State = form["State"].value
		Zipcode = form["Zipcode"].value
		DepartmentId = form["DepartmentId"].value
		Email = form["Email"].value
		Phone = form["Phone"].value
		SupervisorId = form["SupervisorId"].value
		Salary = form["Salary"].value
		dbinterface.updateEmployeeInfo(FirstName,LastName,Gender,Address,City,State,Zipcode,DepartmentId,Email,Phone,SupervisorId,Salary)

	elif "updateEmployeeInfo" in form:
		dbinterface.showUpdateEmployeeInfoForm()

	elif "updateVisitorInfo" in form and "Birthday" in form:
		LastName = form["LastName"].value
		FirstName = form["FirstName"].value
		Address = form["Address"].value
		City = form["City"].value
		State = form["State"].value
		Zipcode = form["Zipcode"].value
		Birthday = form["Birthday"].value
		Email = form["Email"].value
		dbinterface.updateVisitorInfo(LastName,FirstName,Address,City,State,Zipcode,Birthday,Email)

	elif "updateVisitorInfo" in form:
		dbinterface.showUpdateVisitorInfoForm()

	elif "deleteVisitorById" in form and "Id" in form:
		Id = form["Id"].value
		dbinterface.deleteVisitorById(Id)

	elif "deleteVisitorById" in form:
		dbinterface.showDeleteVisitorForm()

	elif "listAnimalInfo" in form and "animalid" in form:
		animalid = form["animalid"].value
		dbinterface.listAnimalInfo(animalid)

	elif "listAnimalInfo" in form:
		dbinterface.showListAnimalInfoForm()

	elif "listNearbyAnimal" in form and "zonename" in form:
		zonename = form["zonename"].value
		dbinterface.listNearbyAnimal(zonename)

	elif "listNearbyAnimal" in form:
		dbinterface.showListNearbyAnimalForm()

	elif "listVisitorBasedOnTier" in form and "tier" in form:
		tier = form["tier"].value
		dbinterface.listVisitorBasedOnTier(tier)

	elif "listVisitorBasedOnTier" in form:
		dbinterface.showListVisitorForm()

	else:        
		# substitute other functions in here to test from command line
		# musicinterface.listArtists()
        
		# show the default page
		dbinterface.showDefaultEmployeePage()

	doHTMLTail()   



					
		