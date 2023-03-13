
# HIT_App: A planner for HIT intervall trainings

### [gitHub Repository](https://github.com/stuWolf/T2A2_API_Training_planer)

### [Source Control](https://github.com/stuWolf/T2A2_API_Training_planer/commits/main)

### [Project Management](https://trello.com/b/2e4HymYf/hit-fit-app)





## R1: Identify the problem you are trying to solve by building this particular app.

My idea is to create an app that can give the user a randomized sequence of HIT (High intensity training) exercises.



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



## R2: Why is it a problem that needs solving?

## 3: Why have you chosen this database system. What are the drawbacks compared to others?

## R4: Identify and discuss the key functionalities and benefits of an ORM
I intend to implement the following functions (routes):

    Register user, admins can delete users
    Admin can add and delete exercises
    A user can generate a workout consistent of 4 HIT exercises chosen randomly out of the exercise table. The user can add some criteria like level or muscle group.
    The workout will be stored in the workout table.
    The user can update the time taken to complete a workout
    The user can delete a workout


## R5: Document all endpoints for your API


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

# DB adaptor for python

pip install psycopg2
pip install flask-sqlalchemy

# password_hash
example:
```py
pw_hash = bcrypt.generate_password_hash('hunter2')
bcrypt.check_password_hash(pw_hash, 'hunter2') # returns True
```

## R8: Describe your projects models in terms of the relationships they have with each other

The database consists of 3 tables: Users, Workouts, exercises and workout_exercises as a mapping table between workouts and exercises.
They can have the following relationships:
-A user can have many workouts; one to many relationship
-A workout consists of many exercises, an exercise can be in many workouts; many to many relationship and will be resolved in the table workout_exercises.

## R9: Discuss the database relations to be implemented in your application
Difference to R8:


## R10: Describe the way tasks are allocated and tracked in your project

![ImplementationPlan](./docs/implementation_plan.png)

08/03 Wednesday
Spec on discord, create ERD
set up structure and DB
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


## Workout_exercises controller:
A user can trigger a function that generate a workout consistent of 4 HIT exercises chosen randomly out of the exercise table.
The user can add some criteria like level or muscle group.
The workout will be stored in the Workout_exercises table.
print all workout_exercises with the same exercise id






