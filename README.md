# 0x00. AirBnB clone - The console

## Description
Web application that simulates some of the features of Airbnb for academic purposes.

In this moment we are the first part "the console"
The console is a way of using the typical functionalities of an administrative panel (for example CRUD) but without a graphical interface because, as its name implies, it is done from a command console.

### Components diagram

<img src="./assets/step1.png"
     alt="img components"
     style="float: left; margin-right: 10px;" />

### Database UML

<img src="./assets/uml.jpg"
     alt="img uml"
     style="float: left; margin-right: 10px;" />


## Prerequisites 📋

64-bit system , Ubuntu 

## Objectives

### Console

-   Create your data model
-   Manage (create, update, destroy, etc) objects via a console / command interpreter
-   Store and persist objects to a file (JSON file)

### Web Static
-   learn HTML/CSS
-   create the HTML of your application
-   create template of each objec

### MySQL storage
-   replace the file storage by a Database storage
-   map your models to a table in database by using an O.R.M.

### MySQL storage
-   replace the file storage by a Database storage
-   map your models to a table in database by using an O.R.M.

### Web framework - templating
-   create your first web server in Python
-   make your static HTML file dynamic by using objects stored in a file or database

### RESTful API
-   expose all your objects stored via a JSON web interface
-   manipulate your objects via a RESTful API

### Web dynamic

-   learn JQuery
-   load objects from the client side by using your own RESTful API

## Console

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine

### How to start the console?
`./console.py`

### How to use the console?
1. Start the console
2. Write the desired command with its respective syntax

Available classes: BaseModel, User, Place, State, City, Amenity and Review

| Command| Syntax| Description|
|---|---|---|
|create|`create <class>`|create a object|
|show|`show <class> <id>`|show an specific object|
|destroy|`destroy <class> <id>`|destroy an specific object|
|all|`all <class>`|show all objects by class|
|all|`all`|show all objects|
|update|`update <class> <attr_name> <new_value>`|update an object with the new values|

other way...

| Command| Syntax| Description|
|---|---|---|
|all|`<class name>.all()`|show all objects by class|
|count|`<class name>.count()`|a counter of specific class|
|show|`<class name>.show(<id>)`|show an specific object|
|destroy|`<class name>.destroy(<id>)`|destroy an specific object|
|update|`<class name>.update(<id>, <attribute name>, <attribute value>)`|update an object with the new values|


3. Press the enter button

### Examples:
- `(hbnb) create User`
- `(hbnb) show User fce12f8a `
- `(hbnb) destroy User fce12f8a `
- `(hbnb) all User `
- `(hbnb) all`
- `(hbnb) update User name holberton`
- `(hbnb) User.all()`
- `(hbnb) User.count()`
- `(hbnb) User.show("246c227a")`
- `(hbnb) User.destroy("246c227a")`
- `(hbnb) User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "first_name", "John")`

## Author :copyright:
* **Carlos Daniel Cortez** - [kael1706](https://github.com/kael1706)
* **Jesus Acevedo Cano** - [Jesus-Acevedo-Cano](https://github.com/Jesus-Acevedo-Cano)
