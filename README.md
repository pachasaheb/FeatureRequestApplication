# Feature Request Application:
	Feature Request Application is built with Python and Flask which is a web application framework written 
	in Python. It consists of feature request form page where a user can fill in a feature request, html 
	values are binded using KnockoutJS,using SqlAlchemy ORM details are persisted in database and 
	feature request details page where a user can see feature request list in the form of a table.
  
 ## Getting Started:
	 Pre-requisites: Project is developed using
	    * Python (v.3.6.4), 
	    * PostgreSql database(v.10.1)
	    * Browsers: Chrome(v.64.) and Firefox(v.55+)
 
## Installation:
1.Download the project folder from the github. Create a Python Virtual Environment. Unzip the project folder 
inside Virtual Environment.

2. For Data Base Connection change the line inside config.py 
db_string = "postgres://postgres:Password0@localhost:5432/featureapp".
Make changes according to your local database and comment the rest of unrequired database connection strings.

3.Uncomment the line inside run_waitress_server.py "serve(APP,host="localhost",port="5000")" to run it on the localhost.

4.Activate the Virtual Environment.
	
5.Then install required packages present in requirements.txt file.

6.Set Flask_APP variable by using command ‘set FLASK_APP=run_waitress_server.py’.

7.Type ‘flask run’ and navigate to ‘http://127.0.0.1:5000/’ you can see Feature Request App form page.
 					
 ## Feature Request Application Form Page:
 	Open chrome/Mozilla and navigate to url ‘http://127.0.0.1:5000/’ where list of fields are present for 
	customer to fill in are as follows:
	1.Title: A short, descriptive name of the feature request.
		•Title [String type] Length-100 characters (Will stop user further entering 100 by using html
		input ‘maxlength’ attribute).
		•Title is unique field (Same titles cannot be entered for different clients).
		•Title is Mandatory field (Input validation is done by html attribute ‘required’).
	2.Description: A long description of the feature request.
		•Description [String type] Length- 1000 characters (Will stop user further entering 1000 by 
		using html input ‘maxlength’ attribute).
		•Description uses ‘text-area’ html input attribute which can be auto align as required by user.
		•Description filed is not mandatory.
	3.Client: A selection list of clients (use "Client A", "Client B", "Client C")
		•Client [String type] will display list with three options "Client A","Client B", "Client C"
		(using html ‘select’ and ‘options’ type attributes) and user can select any one of the clients.
		•Client field is also mandatory
	4.Client Priority: A numbered priority according to the client (1...n).Client Priority numbers should not
	repeat for the given client, so if a priority is set on a new feature as "1", then all other feature 
	requests for that client should be reordered.
		•Client Priority [Integer Type]-User can only enter numbers (Will stop user entering String values,
		by using html input type as ‘number’).
		•Client Priority is mandatory field.
		•User cannot enter any negative values.
		•Client Priority will not be same for two features with respect to a single client as Client 
		Priority will be re-ordered.
	5.Target Date: The date that the client is hoping to have the feature.
		•Target Date [Date type] field displays a calendar (User can select date in the calendar).
		•User can only select future dates and past dates cannot be selected.
		•Target Date is a mandatory field.
	6.Product Area: A selection list of product areas (use 'Policies', 'Billing', 'Claims', 'Reports')
		•Product Area [String Type] field display list of four options 'Policies', 'Billing', 'Claims', 
		'Reports' (using html ‘select’ and ‘options’ type attributes) and user can select any 
		one of Product Area.
		•Product Area is a mandatory field.
    	At the End of page a reference link for 'List of Feature Requests' is present to navigate to Feature
	Request Details Page
        
## Feature Request Application Details Page:
	Entering all values and on clicking ‘Submit’ it will navigate to details page at url ‘http://127.0.0.1:5000
	/FeatureRequestDeatils’ where all the feature request details are reflected in a table [built with jQuery 
	data Table] which will have Sorting and Searching.
## Feature Request Application Update:
	By clicking on title in table in Feature Request Application Details Page a boostrap modal will appear
	with respective Feature Request Details which can be edited and on clicking 'Update' button Feature Request
	Details will get updated in database.
	
## Stack/Application Details:
	The following are requirements on the tech stack. This stack demonstrates mastery of tools our team favors.
	•OS: Windows/Linux
	•Server Side Scripting: Python (3.6.4)
	•Server Framework: Flask (0.12.2)
	•SqlAlchemy (1.2.2): Solution Options for Reprioritization
		1.SQL ORM: This has been implemented-ORM tools provide an object oriented query language. This allows
		application developers to focus on the object model and not to have to be concerned with the database
		structure or SQL semantics.The ORM tool itself will translate the query language into the appropriate
		syntax for the database.
		2.Using Stored Procedure: Stored procedures are compiled once and stored in executable form, so 
		procedure calls are quick and efficient. Executable code is automatically cached and shared among 
		users. This lowers memory requirements and invocation overhead.
		3.Bulk Update: A feature which will record all the changes and will update in bulk which will reduce
		the detours to/from database.
	•JavaScript: KnockoutJS (3.4.2): Knockout is a JavaScript library that which gives a simplified and dynamic 
	Model-View-View Model binding pattern for all the UI elements in HTML.
	•Testing: Unittest2 (1.1.0): Using Unittest in python test cases have been written to test positive and negative 
	 workflow of code. 


       
