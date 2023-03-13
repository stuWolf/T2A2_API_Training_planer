Setup your Flask App
- design for development
- we will create and activate virtual environment
- add flask to requirement file
- pip install dependencies through requirement txt
- configuration of the App
- need to setup my app with filename main.py
- define FLASK_APP environment
- create function to initialize app

- Thinking to use MVC
- Model, view, controller, db
- db √
- view  <-> schema √
- controller √
- model √

- git initialize

- setup sql alchemy
- setup marshamallow (req <-> res)
- setup command line expression (DDL -> DB)


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
Start documentation, readme

14


## Workout_exercises controller:
A user can trigger a function that generate a workout consistent of 4 HIT exercises chosen randomly out of the exercise table.
The user can add some criteria like level or muscle group.
The workout will be stored in the Workout_exercises table.
print all workout_exercises with the same exercise id



## Readme file

R1: Identify the problem you are trying to solve by building this particular app.

R2: Why is it a problem that needs solving?

R3: Why have you chosen this database system. What are the drawbacks compared to others?

R4: Identify and discuss the key functionalities and benefits of an ORM

R5: Document all endpoints for your API

R6: ERD

R7:  Detail any third party services that your app will use

R8: Describe your projects models in terms of the relationships they have with each other

R9: Discuss the database relations to be implemented in your application

R10: Describe the way tasks are allocated and tracked in your project