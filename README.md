# Zoo-Database
CS220 Final Project: Design a zoo database

Zoo Management System:
Main Idea: The main purpose of the application is to have a relational database among the administrator, Employees,User/Visitors and the animals in the zoo. The main user of the application will be the Administrator and the visitors. The administrator will have access to the employee information such as who is employed, how long they have been employed, their salary, which animal department they work for etc. Other access the administrator will have is the animal information like the types of animals stores, how much food, how long in captivity, their BOD etc. Lastly, the administrator can also have access to the Visitor information, to see how many visitors come in, which animals they visit etc. The visitors will have access to information of animals such as origins, breed, species, etc and their profile such as booking, ticket payment, or if they are join membership program of the zoo.
User Stories: Administrator will have the task of adding say when a new employee is hired,a new animal joins the zoo, updating information about the animals or about the employees, deleting records say when an employee or an animals leaves the zoo by filling appropriate form after declaring what types of action they want to perform. The visitors can add a new account and update their profiles whenever they need to by filling exact information such as email and password and pay for tickets or donation with valid card information.
 
Data Requirements: the ER link is:
https://www.lucidchart.com/invitations/accept/a9636309-91b3-4add-a5a1-941f23893388
Functionality requirements: the user centric design
The context of use: the administrator and the visitor will be using it to gain access to update, add, delete information as mentioned before in the user story.
Requirements: fulfill all the hardware and software system requirements like an sql server so there is proper access to all the real time update information. To get the high number of visitors, the animals records should be updated consistently. In addition, the application is able to provide administrators specifically needed data to analyse and to compute and return desired results such as minimum/maximum profit changes during a period of time or map functionalities such as best way to tour around the zoo, where to put a new animal physically onto the zoo territory.
Design solutions: Limit the access of visitors and employees to the entire database and have strict login requirement for security and include layers of abstraction between retrieving the data and the actual implementation of algorithms.

Database functionalities and design is found in "CS220 - Final Project.pdf".
