Products API - Backend
Project
Tech Stack
Python, Flask, Postman 

Main Stories


(5 points): As a developer, I want to make good, consistent commits.
(2.5 points): As a developer, I want to create an Entity Relationship Diagram that will accurately show the necessary properties on the Product model.
Be sure to include a screenshot of your ERD in your GitHub repository!
(5 points): As a developer, I want to build a REST web API in Flask, so that I can make HTTP requests interact with the data set.
(2.5 points): As a developer, I want to create a Product model
Property names must be in snake_case and match the following exactly!
id - Integer
name - String
description - String
price - Float
inventory_quantity - Integer


(5 points): As a developer, I want my API to serve content on the following url paths:
    Paths must match these exactly!
    ‘127.0.0.1:5000/api/products/' 
    ‘127.0.0.1:5000/api/products/<int:pk>’ 

(5 points): As a developer, I want to create a GET endpoint that responds with a 200 success status code and all of the products within the Product table.
(5 points): As a developer, I want to create a GET by id endpoint that does the following things:
    Accepts a value from the request’s URL (The id of the product to retrieve).
    Returns a 200 status code. (Explicitly return this, not just allow it to default)
    Responds with the product in the database that has the id that was sent through the URL. 

(5 points): As a developer, I want to create a POST endpoint that does the following things:
    Accepts a body object from the request in the form of a Product model. 
    Adds the new product to the database. 
    Returns a 201 status code. 
    Responds with the newly created product object.

(5 points): As a developer, I want to create a PUT endpoint that does the following things:
    Accepts a value from the request’s URL (The id of the product to be updated). 
    Accepts a body object from the request in the form of a Product model. 
    Finds the product in the Product table and updates that product with the properties that were sent in the request’s body. 
    Returns a 200 status code.  (Explicitly return this, not just allow it to default)
    Responds with the newly updated product object. 

(5 points): As a developer,  I want to create a DELETE endpoint that does the following things:
    Accepts a value from the request’s URL. 
    Deletes the Product from the database.
    Returns a 204 status code (NO CONTENT).


(5 points): As a developer, I want to use Postman to make a POST, PUT, DELETE, and both GET requests (get by id and get all)  request to my REST web API, save it to a collection, and then export it as a JSON from Postman.
    Be sure to include the exported JSON file in your project folder and push it to GitHub!


Bonus Stories
(5 points): As a developer, I want to add the ability to add an image link to each product. (Link to picture on the internet, this column will just be a simple String representing the URL of the image, you do NOT need to add an actual image file.) 

Checklist

Run through the Setup Setups and get your project ready to begin work.
Review the Resources outlined below - be sure to have relevant documentation and references open while you develop!

Setup Steps
Download and extract the zip file from the starter code repo, open in VS Code.
Create your own Github repo with a Python gitignore and your own README, then push the code up.
Create a MySQL Database with an appropriate name for the project.
Change the username,  password and db_name in the .env file to your MySQL username/password and the database you just created.
NOTE: Some special characters in the password (especially @ and /) must be url escaped. For a @, use %40. For a /, use %2F
Create your virtual environment with terminal commands:
pipenv install
pipenv shell
Once the venv is created, you can start the app at any time with flask run
Create your database model(s) in app.py with the required properties, then run:
flask db init (Creates tables)
flask db migrate -m "Init" (Creates migration)
flask db upgrade (Runs migration)
Create Marshmallow Schema in app.py
Continue on to create Resource classes and Routes, making sure to test each endpoint in Postman!

Resources

PowerPoints
HTTP JSON Request Response 
REST API
Postman
Flask

Other Resources 	
Flask Tutorial Series


End Result  
The result of your Products API backend will be the execution of requests made in Postman. You must test your Products API by executing each request you create in Postman.  
