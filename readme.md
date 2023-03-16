
# HIT_App: A planner for HIT intervall trainings

### [gitHub Repository](https://github.com/stuWolf/T2A2_API_Training_planer)

### [Source Control](https://github.com/stuWolf/T2A2_API_Training_planer/commits/main)

### [Project Management](https://trello.com/b/2e4HymYf/hit-fit-app)





## R1: Identify the problem you are trying to solve by building this particular app.

My idea is to create an app that can give the user a randomized sequence of HIT (High intensity training) exercises in the entity "workouts". 



## Setup
### 1. create and connect to db
sudo -u postgres psql
CREATE DATABASE fitt_api_db;
DROP DATABASE 


### 2. Create user for DB, grant all permissions
CREATE USER db_dev WITH PASSWORD '123456';
GRANT ALL PRIVILEGES ON DATABASE fitt_api_db TO db_dev;

### 3. connect to DB
\c fitt_api_db;

### 4. initialise program


## R2: Why is it a problem that needs solving?

## 3: Why have you chosen this database system. What are the drawbacks compared to others?
I choose postgreSQL because it is a free and open-source relational database management system (RDBMS) emphasizing extensibility and SQL compliance. It is commonly known as Postgres, and it was developed to provide an open-source alternative to commercial databases like Oracle and Microsoft SQL Server.
It is widely used and known for its reliability, stability, and security, it is also a popular choice for mission-critical applications. Additionally, PostgreSQL supports several advanced data types, indexing options, and transaction management.


PostgreSQL has the following Advantages:
1. It is open-source software, what makes it a cost-effective solution. 
2. It has a large and active community of developers, users, and contributors, so there are lots of resources and support available.
3. It is known for its performance, especially for complex queries and large amounts of data. It also provides a number of features for optimizing performance, such as indexing and caching. (in caching frequently accessed data in cach memory for faster access)
4. It can handle large amounts of data and can be easily scaled to meet the needs of growing organizations.
5.	Advanced Data Types: It supports a wide range of data types, including geographic data types, arrays, and hstore (a key-value store).


Disadvantages:
1. Postgres has a steep learning curve for new users, especially those who are not familiar with SQL or relational databases.
2.	 While PostgreSQL has a strong community of users and contributors, it may not have the same level of commercial support as proprietary databases like Oracle or Microsoft SQL Server.
3.	Limited Windows Support: While it runs on Windows, it is more commonly used on Unix and Linux platforms, and some features may not be fully supported on Windows.
4. PostgreSQL does not have native support for mobile platforms, which can limit its use for mobile applications.
5. Configuring and maintaining PostgreSQL can require a significant amount of effort and technical knowledge, especially for large and complex installations.


[1] Cloudflare
## R4: Identify and discuss the key functionalities and benefits of an ORM

An ORM (Object-Relational Mapping) is a programming technique that enables developers to work with relational databases using object-oriented programming languages. It provides a set of APIs that abstract away the details of the underlying database and allow developers to interact with data as objects. The key functionalities and benefits of an ORM are:

    Database Abstraction: An ORM provides an abstraction layer between the application and the database. It abstracts away the details of the underlying database, such as SQL queries, data types, and data conversions, and allows developers to interact with the database using objects and methods. This makes it easier to work with databases and reduces the complexity of database interactions.

    Object-Relational Mapping: An ORM maps objects to database tables and vice versa. It provides a way to represent database tables as classes and records as objects. This makes it easier to work with data, as developers can use object-oriented programming concepts, such as inheritance, polymorphism, and encapsulation, to manipulate data.

    CRUD Operations: An ORM provides APIs for creating, reading, updating, and deleting records in the database. This makes it easier to perform CRUD operations, as developers can use object-oriented concepts to manipulate data, rather than writing SQL queries.

    Query Building: An ORM provides APIs for building complex queries, such as joins, filters, and aggregations ("has-a" relationship between objects). This makes it easier to construct complex queries, as developers can use object-oriented concepts to build queries.

    Portability: An ORM allows the same code can be used to interact with different databases (database-agnostic code), without changing the code. This makes it easier to switch between databases, as the ORM handles the differences between databases.

    Maintainability: The code can be easily maintained and updated, without affecting the underlying database schema. This makes it easier to update the application, as the ORM handles the changes to the database schema.




## R5: Document all endpoints for your API
## preparatoins to run the program
## Setup
### 1. create and connect to db
sudo -u postgres psql
CREATE DATABASE fitt_api_db;


### 2. Create user for DB, grant all permissions
CREATE USER db_dev WITH PASSWORD '123456';
GRANT ALL PRIVILEGES ON DATABASE fitt_api_db TO db_dev;

### 3. connect to DB
\c fitt_api_db;

### 4. initialise program
change to T2A2_API_WEB
flask init
# Login





# create workout

# Ammend and delete workout (only admin or user who created workout)

# create, ammend and delete exercise (admin only)


# Create workout exercise ( randomly choose 4 exercises from exercises list)

# print out all exercises of a workout id
# fetch all exercises of under a workout id number from Workout_exercises 
# look up exercises for each exercise id and print them out


I intend to implement the following functions (routes):

    Register user, admins can delete users
    Admin can add and delete exercises
    A user can generate a workout consistent of 4 HIT exercises chosen randomly out of the exercise table. The user can add some criteria like level or muscle group.
    The workout will be stored in the workout table.
    The user can update the time taken to complete a workout
    The user can delete a workout




### User controller:
1. Login:
HTTP Request:
http://localhost:5000/users/login

Input:
```json
http://localhost:5000/users/login
 {   
    "email": "wolf@gmail.com",
        "password": "dudrst"

}

Output
```

## R6: ERD

## R7:  Detail any third party services that your app will use
- The required dependencies can be found in the requirements.txt file, located at ```T2A2_API_WEB/requirements.txt```. 
I outline the most important packages used:
# ORM:  
flask-sqlalchemy , explanation please see R4

# flask Marshmallow: 
To serialize data and convert python objects to JSON or vice versa

#  Bcrypt()
password hashing function
Bcrypt  is a cryptographic algorithm that generates a one-way hash of a password, which makes it difficult for an attacker to obtain the original password, even if they gain access to the stored hash, it is considered to be one of the most secure password-hashing functions available today and is recommended by security experts for use in applications that require strong password protection.
example:
```py
pw_hash = bcrypt.generate_password_hash('hunter2')
bcrypt.check_password_hash(pw_hash, 'hunter2') # returns True
```
#  JWTManager()

This library offers the functions to verify the authenticity of JSON Web Tokens (JWTs). we use here create_access_token, jwt_required, get_jwt_identity.
@jwt_required() only allows a function to be executed after sucessfull verification of user access token. 
get_jwt_identity returns the user id of the logged in user.


## R8: Describe your projects models in terms of the relationships they have with each other

The database consists of 4 tables: users in model User, workouts, implemented in model Workout, exercises implemented in model Exercise and workout_exercises  model Workout_Exercise as a mapping table between workouts and exercises.
They can have the following relationships:
-A user can have many workouts; This is a one to many relationship
-A workout consists of many exercises and an exercise can be in many workouts; This is a  many to many relationship and will be resolved in the table workout_exercises.

## R9: Discuss the database relations to be implemented in your application
-A user can have many workouts; This is a one to many relationship. Therefore Workouts will have the foreign key "user_id"
-A workout consists of many exercises and an exercise can be in many workouts; They are oin a many to many relationship and will be resolved in the table workout_exercises.
Workout_Exercises will have two foreign keys "workout_id" and "exercise_id"


## R10: Describe the way tasks are allocated and tracked in your project

![ImplementationPlan](./docs/implementation_plan.png)

## Run journal and todo list:
08/03 Wednesday
put Spec on discord, create ERD
set up structure and DB
Planned functions to be implemented:
    Register user, admins can delete users
    Admin can add and delete exercises
    A user can generate a workout consistent of 4 HIT exercises chosen randomly out of the exercise table. The user can add some criteria like level or muscle group.
    The workout will be stored in the workout table.
    The user can update the time taken to complete a workout
    The user can delete a workout

09/03 Thursday
## user controller, authorisation
Register user, admins can delete users

10/03 Friday
Figure out schemas, nested
## exercise controller functions:
Admin can add and delete exercises

11/03 Sat
## workout controller:
print all workouts of a certain user
The user who created it can update the time taken to complete a workout, delete a workout

12/03 Sun
Implemented Function to choose 4 exercises out of the exercise table in exercise controller and store the relation in the workout_exercises table
This functin is triggered when creating a workout
Display all exercise based on a workout Id workout controller, function to pick 4 random exercises

13/03 Mon
Update workout function: make sure that user can not change the name to an existing name
Start documentation
14/03 Tue
Introduced new table Exercise_filter. The Idea was to filter exercises by level and body region and store the result in this table, than choose 4 random exercises for the training out of that selection.
It looks like it is session.bulk_insert_mappings(MyTable, rows_to_insert) after all. 
In the end I solved the problem by drawing a random exercise first and than checking if it matches the criteria. if yes, store the result in workout_exercises if not, draw next exercise and check until  found 4 exercises.
15/03 Wed
Tried session.bulk_insert_mappings(MyTable, rows_to_insert) , initialise table on its own but no success
Issues with .first()  exercises = Exercise.query.filter_by(body_region=body_region).first()
object not collatable error
Documentation

16/03 Thursday
System overview: List down all routes, test plan, explanation
Test plan: Endpoint,  test data, expected return, result
Exception handling: wrong or missing key

17/03 Friday
to do: Implement exception handling for all functions/Routes
Test,  continue on questions , R1, 2, R4, document endpoints


## Workout_exercises controller:
A user can trigger a function that generate a workout consistent of 4 HIT exercises chosen randomly out of the exercise table.
The user can add some criteria like level or muscle group.
The workout will be stored in the Workout_exercises table.
print all workout_exercises with the same exercise id






