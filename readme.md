
# HIT_App: A planner for high intensity intervall trainings (HIT)

### [gitHub Repository](https://github.com/stuWolf/T2A2_API_Training_planer)

### [Source Control](https://github.com/stuWolf/T2A2_API_Training_planer/commits/main)

## R1: Identify the problem you are trying to solve by building this particular app.
The bedrocks of any good workout routine should be:
- Tracking progress, helps to stay motivated and see tesults
- Variating the exercises: It is important to variate the exercise and sequence to keep the body guessing, avoid boredom and increase motivation.
- Having an adequate workout plan
- Correct posture: An exercise done with the wrong posture and body possition can lead to injuries. Having at least a photo as reminder would be helpful.

Therefore instead of runing around with a sheet of paper it would be very helpful to create an app that shows a sequence of exercises, time interval or reps for every exercise, tips about the exercise (posture), show a picture or video, something like an electronic personal trainer. At the end of the workout the user can monitor his progres, with data such as rounds completed, body weight, time taken to complete the workout or mody meashurements. The program could also make suggestions about increasing level of difficulties.
My idea is to create an app that can give the user a randomized sequence of HIT (High intensity training) exercises, stored in the entity "workouts". it draws 4 randomm exercises from a list of exercises. The program applies a filter based on the criterias "level" and "body region" defined in the workout.

## R2: Why is it a problem that needs solving?

The potential benefits of having a fitness planing app:
1.	Personalisation: Being able to create personalized fitness plans based on an individual's goals, and fitness level. 
2.	A fittness app will help to stay on track with  fitness goals by providing reminders and encouragement to exercise. This can help individuals to stay motivated and committed to exercising.
3.	Cost-savings: Hiring a personal trainer can be expensive, but a fittness app automises big parts of that service and can provide guidance and support at a fraction of the cost. 
4.	Convenience: The app can be accessed from anywhere at any time, making it a convenient option for individuals with busy schedules or limited access to fitness facilities.
5.	progress tracking: A fittness app can track progress over time. This can help individuals to make adjustments to their workouts and achieve their goals more effectively.


## R3: Why have you chosen this database system. What are the drawbacks compared to others?
I choose postgreSQL because it is a free and open-source relational database management system (RDBMS) emphasizing scalability and SQL compliance. It is commonly known as Postgres, and it was developed to provide an open-source alternative to commercial databases like Oracle and Microsoft SQL Server.
It is widely used and known for its reliability, stability, and security.  Additionally, PostgreSQL supports several advanced data types, indexing options, and transaction management.


PostgreSQL has the following Advantages:
1. It is open-source software, what makes it a cost-effective solution. 
2. It has a large and active community of developers, users, and contributors, so there are lots of resources and support available.
3. It is known for its performance, especially for complex queries and large amounts of data. It also provides a number of features for optimizing performance, such as indexing and caching. (in caching frequently accessed data in cach memory for faster access)
4. It can handle large amounts of data and can be easily scaled to meet the needs of growing number of users and exercises.
5.	Advanced Data Types: It supports a wide range of data types, including geographic data types, arrays, and hstore (a key-value store).
6. Data Integrity: PostgreSQL provides robust data validation and integrity checks, which ensure the consistency and accuracy of data.
7. The database runs on an external database server what is basically what I need because the users should be able to access a shared pool of exercises, continuously updated by the administrator


Disadvantage:
Further research has shown that especially for an application like Fitt APP which runs mostly on mobile platforms postgres has some setbacks:

1. PostgreSQL does not have native support for mobile platforms, which can limit its use for mobile applications.

2. PostgreSQL can be more complex to set up and configure than SQLite, and may require a separate database server, which can increase the complexity of the app. Additionally, it may require more system resources than SQLite, which can impact the app's performance on mobile devices with limited resources.

Overall, while PostgreSQL is a powerful and capable RDBMS, it may not be the most suitable choice for a mobile fitness planning app that requires efficient and lightweight storage, and which is primarily focused on user interaction and ease of use. For my first app I still decided to use PostgreSQL because that's what I am most famillar with and the app needs to store shared information like the exercises and user profile data on an external server. 
But If I want to take the App further, develop a front end and put it on a production server I might consider converting it to SQLite. I red that  it is possible to implement mechanisms such as Content Providers or a client-server model to allow multiple users to share data

[1] Cloudflare
## R4: Identify and discuss the key functionalities and benefits of an ORM

An ORM (Object-Relational Mapping) is a programming technique that enables developers to work with relational databases using object-oriented programming languages. It provides a set of APIs that abstract away the details of the underlying database and allow developers to interact with data as objects. The key functionalities and benefits of an ORM are:

    Database Abstraction: An ORM provides an abstraction layer between the application and the database. It abstracts away the details of the underlying database, such as SQL queries, data types, and data conversions, and allows developers to interact with the database using objects and methods. This makes it easier to work with databases and reduces the complexity of database interactions.

    Object-Relational Mapping: An ORM maps objects to database tables and vice versa. It provides a way to represent database tables as classes and records as objects. This makes it easier to work with data, as developers can use object-oriented programming concepts, such as inheritance, polymorphism, and encapsulation, to manipulate data.

    CRUD Operations: An ORM provides APIs for creating, reading, updating, and deleting records in the database. This makes it easier to perform CRUD operations, as developers can use object-oriented concepts to manipulate data, rather than writing SQL queries.

    Query Building: An ORM provides APIs for building complex queries, such as joins, filters, and aggregations ("has-a" relationship between objects). This makes it easier to construct complex queries, as developers can use object-oriented concepts to build queries.

    Portability: An ORM allows the same code to be used to interact with different databases (database-agnostic code), without changing the code. This makes it easier to switch between databases, as the ORM handles the differences between databases.

    Maintainability: The code can be easily maintained and updated, without affecting the underlying database schema. This makes it easier to update the application, as the ORM handles the changes to the database schema.




## R5: Document all endpoints for your API

To keep the readme file at a reasonable sice, I document here the endpoints requiring data input. For the remaining functions please 
refer to System Overview and Test Plan

[Test Plan](./docs/Fit_API_Test_Plan.pdf)

[System Overview](./docs/Fit_API_System_overview.pdf)

## 1. Entity: Users 
module: user_controller.py

### 1.1. Login: 
HTTP Request(POST):  http://localhost:5000/users/login


```json
Input:
 {   
    "email": "wolf@email.com",
        "password": "pword123"

}

Output
{
    "_comment": "Login suceeded:",
    "admin": false,
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY3OTAxMjIzMywianRpIjoiMDgzMzYwOTctODk1Yi00OTlkLTk1YWUtN2I3NDFmY2NhYjVkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjMiLCJuYmYiOjE2NzkwMTIyMzMsImV4cCI6MTY3OTA5ODYzM30.LIzpmtw76MoiVkpvke83wfbPs-8BNokA5R5ZStndjis",
    "user": "wolf@email.com",
    "user_id": 3
}
```
### 1.2 Register new user
Authentication: none
HTTP request (POST): http://localhost:5000/users
```json
Input:
{
    "admin": false,
    "email": "wolf@mail.com",
    "mobile_number": "345345353",
    "username": "Wolfee Puck",
    "password": "12345"
    
}
Output:
{
    "admin": false,
    "email": "wolf@mail.com",
    "id": 4,
    "mobile_number": "345345353",
    "password": "$2b$12$jponP3B6qwKMq9unKgeySubRK5/c7N0rXSFGd53kPVShb1q28pwKC",
    "username": "Wolfee Puck"
}
```

### 1.3 Delete User (admin or user can delete himself )
Authentication: user or admin login
HTTP request (DELETE): http://localhost:5000/users/wolf@mail.com  (user email)

```json
Input: email as arg in HTTP request
Output:
{
    "_comment": "deleted:",
    "user": "wolf@mail.com",
    "user_id": 4
}
```

### 1.4 Amend User (only by the user itself)
Authentication: user  login
HTTP request (PUT): http://localhost:5000/users/update
```json
input:
{
    "admin": false,
    "email": "wolf@mail.com",
    "mobile_number": "345345353",
    "username": "Wolfgang Puck",
    "password": "12345"
}
Output:
{
    "_comment": "updated:",
    "usename": "Wolfgang Puck",
    "user": "wolf@mail.com",
    "user_id": 5
}

```

## 2. Entity:  Workouts
module: workout_controller.py

### 2.1 Create new workout with logged in user
Authentication: user  login
HTTP request (POST): http://localhost:5000/workouts

This is the core function of this API. when the workout gets created the function calls workout_exe_controller.pick_exercises(workout_id, body_region, level) which selects 4 exercises out of the exercises table based on body_region and level.  the result is stored in workout_exercises and can be displayed in http://localhost:5000/workout_exercises/"workout name"
```json
Input:
{
    "workout_name": "Cardio",
    "rest_time": "1 min",
    "rounds": "8 rounds",
    "body_region": "cardio",
    "level": "",
    "progres": "15 min"
}
Output:
{
    "body_region": "cardio",
    "date": "2023-03-17",
    "id": 4,
    "level": "",
    "progres": "15 min",
    "rest_time": "1 min",
    "rounds": "8 rounds",
    "user": {
        "email": "wolf@mail.com"
    },
    "workout_name": "Cardio"
}
```

### 2.2 Delete workout (only admin or user who created it)
Authentication: user or admin login
HTTP request (DELETE): http://localhost:5000/workouts/Cardio

```json
Output:
{
    "_comment": "deleted:",
    "workout_name": "Cardio",
    "workout_user": 5
}
```

### 2.3 Amend workout (only user who created it)

Authentication: user  login
HTTP request (PUT): http://localhost:5000/workouts/update/Core2

```json
Input:
{
    "workout_name": "Cardio2",
    "rest_time": "8 min",
    "rounds": "max rounds in 15 min",
    "body_region":"Cardio",
    "level": "hard",
    "progres": "5 rounds"
    
}
Output:
{
    "body_region": "Cardio",
    "date": "2023-03-17",
    "id": 5,
    "level": "hard",
    "progres": "5 rounds",
    "rest_time": "8 min",
    "rounds": "max rounds in 15 min",
    "user": {
        "email": "wolf@mail.com"
    },
    "workout_name": "Cardio2"
}
```

## 3. Entity Workout_exercises
module: workout_exe_controller.py
### 3.1 Display all exercises belonging to a workout

Authentication: none
HTTP request (PUT): http://localhost:5000/workout_exercises/Upper B

Besides creating a workout, this is the most important function of this API because this should be the interface for the front end to display the exercises of a workout one by one
with the required extra information like timer and photo 
```json
Input: workout name as http request argument (here "Upper B")
Output:
[
    {
        "date": "2023-03-17",
        "exercise": {
            "body_region": "lats, arms",
            "description": "deploy core",
            "interval_time": "na",
            "level": "hard",
            "name": "Pull Ups",
            "repetitions": "10",
            "video": null,
            "weight": null
        },
        "workout": {
            "rest_time": "1 min",
            "rounds": "5",
            "workout_name": "Upper B"
        }
    },
    {
        "date": "2023-03-17",
        "exercise": {
            "body_region": "chest",
            "description": "hold back streight",
            "interval_time": "na",
            "level": "medium",
            "name": "Push Ups",
            "repetitions": "20",
            "video": null,
            "weight": null
        },
        "workout": {
            "rest_time": "1 min",
            "rounds": "5",
            "workout_name": "Upper B"
        }
    }
]
```
### 3.2 Manually add exercises to  workout
Authentication: user or admin login
HTTP request (PUT): http://localhost:5000/workout_exercises/Cardio3 

Gives the user the option to manually add an exercise to an existing workout
```json
Input:
workout name in HTTP request (here cardio3)
and id of exercise to be added
{
    "exercise_id": "11"
}
Uutput:
{
    "Exercise id": 11,
    "added Exercise": "sit up2",
    "to workout": "Cardio3 "
}
```

## 4. Entity Exercises
module: exercise_controller.py

### 4.1 Amend exercise (only admin)

Authentication: admin  login

HTTP request (PUT): http://localhost:5000/exercises/update
As we use the unique name in the Json request form to identify the record to be changed, the name can not be changed becaus it would trigger existing name error.
```json
Input:
{
    "description": "Back streight",
    "interval_time": "2 min",
    "level": "easy",
    "body_region": "shoulder",
    "name": "Inverted Row",
    "repetitions": "Max reps",
    "weight": "na"
}
Output:
{
    "_comment": "updated:",
    "exercise Name": "Inverted Row",
    "exercise_id": 2,
    "level": "easy",
    "user": "admin@email.com"
}
```
### 4.2 Create exercise (only admin)

Authentication: admin  login
HTTP request (POST): http://localhost:5000/exercises

```json
Input:
{
    "name": "Chest clap push ups",
    "description": "back sreight",
    "interval_time": "3 min",
    "repetitions": "max reps",
    "body_region": "core",
    "level": "easy",
    "weight": "",
    "video": "a video"
}
Output:
{
    "body_region": "core",
    "description": "back sreight",
    "interval_time": "3 min",
    "level": "easy",
    "name": "chest clap push ups",
    "repetitions": "max reps",
    "video": "a video",
    "weight": ""
}
```

### 4.2 Delete exercise (only admin)

Authentication: admin  login
HTTP request (Delete): http://localhost:5000/exercises/4

```json
Input:
Exercise Id in HTTP request
Output:
{
    "_comment": "deleted:",
    "exercise_id": 4,
    "name": "Sit Ups"
}
```
## 5. Entity:  Progres
module: progres_controller.py

### 5.1 Create new progres record with the user id of logged in user
Authentication: user  login
HTTP request (POST): http://localhost:5000/progresses

```json
Input:
{
    "progres_name": "Advanced4",
    "weight": "85kg",
    "mid_arm": "35cm",
    "waist": "100cm",
    "chest": " 108cm",
    "hip": "100cm",
    "test_score": "200 p"
}
Output:
{
    "chest": " 108cm",
    "date": "2023-03-19",
    "hip": "100cm",
    "id": 5,
    "mid_arm": "35cm",
    "progres_name": "Advanced4",
    "test_score": "200 p",
    "user": {
        "email": "wolf@email.com"
    },
    "waist": "100cm",
    "weight": "85kg"
}
```
### 5.2 print all progres records of logged in user
Authentication: user  login
HTTP request (GET): http://localhost:5000/progresses
Output: all user records

### 5.3 update progress record
Authentication: user  login
HTTP request (PUT): http://localhost:5000/progresses/update/Advanced2

```json
Input:
{
    "progres_name": "Advanced2",
    "weight": "85kg",
    "mid_arm": "35cm",
    "waist": "100cm",
    "chest": " 108cm",
    "hip": "100cm",
    "test_score": "200 p"
}
Output:
{
    "chest": " 108cm",
    "date": "2023-03-19",
    "hip": "100cm",
    "id": 1,
    "mid_arm": "35cm",
    "progres_name": "Initi",
    "test_score": "200 p",
    "user": {
        "email": "wolf@email.com"
    },
    "waist": "100cm",
    "weight": "85kg"
}
```



## Preparatoins to run the program
## Setup
### 1. create  db
sudo -u postgres psql
CREATE DATABASE fitt_api_db;


### 2. Create user for DB, grant all permissions
CREATE USER db_dev WITH PASSWORD '123456';
GRANT ALL PRIVILEGES ON DATABASE fitt_api_db TO db_dev;

### 3. connect to DB
\c fitt_api_db;

### 4. initialise program
change to T2A2_API_WEB/src then flask db init









## R6: ERD
The API has the following entities:
- Users:  Manage User data and access

    attributes : id, Email, Password, Admin, username, mobile_number

 - Workouts: Manage Workout data

    attributes: id, workout_name, rest time, rounds, body_region, level, progres, date, , foreign key: user id

- Progres: manage progres records

    attributes: id, progres_name, weight, mid_arm, waist, chest, hip, test_score_date, foreign key: user id

- Workout_exercises: mapping table between workouts and exercises

    attributes: id, date, foreign keys: workout_id, exercise_id

- Exercises: Manage exercise data

    attributes: id, name, description, interval_time, repetitions, body_region, level, weight

[ERD (PDF)](./docs/Fittnes_API_ERD.pdf)

![ERD](./docs/Screenshot_ERD.jpg)

## R7:  Detail any third party services that your app will use
- The required dependencies can be found in the requirements.txt file, located at ```T2A2_API_WEB/requirements.txt```. 

I outline here the most important packages used:

## flask-sqlalchemy:
ORM, explanation please see R4

## flask Marshmallow: 
To serialize data and convert python objects to JSON or vice versa

##  Bcrypt:
password hashing function
Bcrypt  is a cryptographic algorithm that generates a one-way hash of a password, which makes it difficult for an attacker to obtain the original password, even if they gain access to the stored hash, it is considered to be one of the most secure password-hashing functions available today and is recommended by security experts for use in applications that require strong password protection. As the algorithm is only one way, the only setback is that the user can not send himself a lost password email (as the password is stored in encripted form and can not be decripted). The administrator would  have to assign a new password.
example:
```py
pw_hash = bcrypt.generate_password_hash('hunter2') # creates encrypted password pw_hash
bcrypt.check_password_hash(pw_hash, 'hunter2') # returns True
```
##  JWTManager:

This library offers the functions to verify the authenticity of JSON Web Tokens (JWTs). we use here create_access_token, jwt_required, get_jwt_identity.
@jwt_required() only allows a function to be executed after sucessfull verification of user access token. 
get_jwt_identity returns the user id of the logged in user.


## R8: Describe your projects models in terms of the relationships they have with each other

The database of this API nsists of 5 Models which are:
 - User model
 - Pregres reccord model
 - Workout model
 - Exercise model 
 - Workout_Exercise model
 The user model will include attributes such as user name, email, password, Administrator and mobile number. 
 
 It will be associated with:

1. Workout Model: It includes the following attributes: Workout name, rest time, Rounds completed, body region, level, progres (time or number of rounds completed). The workout models will belong to the user model.

2. Progress Record Model: It will include the attributes name, weight, body measurements, date created and test score of a reference workout. The progress tracker model will belong to the user model.

Exercise Model: The exercise model will include the attributes such as name, description, Interval time, repetitions, video demonstration (or picture), difficulty level, and body region. The exercise model will be associated with the workout model.

The Workout Exercises model acts as a map to assign exercises to workouts.


## R9: Discuss the database relations to be implemented in your application
The API uses the following database relations:

- User and workouts:  
A user can have many workouts dependent on body region and difficulty level; This is a one to many relationship. Therefore Workouts will have the foreign key "user_id"
- User and progres records:  
 This relation will be a one-to-many relation, as each user can have multiple progress records over time, but each progress record will belong to only one user.
Therefore progres records will have the foreign key "user_id"
- Workout and exercises:
A workout consists of many exercises and an exercise can be in many workouts; They are in a many to many relationship and will be resolved in the table workout_exercises.
Workout_Exercises will therefore have two foreign keys "workout_id" and "exercise_id"

Future expanshions:
implement training plan: User has one to many relationship with training plan, training plan has one to many relationship with workout
Autogenerate training plan consistant of different workouts, based on user information like training goal, fitness level, health history and progress. This could also require to determine the fittness level with a fittness test. Also the progress could be monitored by repeating the fittness test every period of time.

## R10: Describe the way tasks are allocated and tracked in your project
### [Project Management](https://trello.com/b/2e4HymYf/hit-fit-app)

![ImplementationPlan](./docs/Screenshot_trello.jpg)

## Run journal and todo list:

Review every morning the previous day and plan the next day


### 08/03 Wednesday
put Spec on discord, create ERD and 
set up structure in VS code and postgres data base.

Planned functions to be implemented:

    -Register user, 
    -admins can delete users
    -Admin can add and delete exercises
    -A user can generate a workout consistent of 4 HIT- exercises chosen randomly out of the exercise table. -The user can add some criteria like level or muscle group.
    -The workout will be stored in the workout table.
    -The user can update the time taken to complete a workout as progres monitoring
    -The user can delete a workout

### 09/03 Thursday
### user controller functions, authorisation

Register user, admins can delete users

### 10/03 Friday

Figure out schemas, nested
### exercise controller functions:
Admin can add and delete exercises

### 11/03 Sat
### workout controller:
print all workouts of a certain user
The user who created it can update the time taken to complete a workout, delete a workout

### 12/03 Sun
### workout_exercise controller:
Implemented Function to choose 4 exercises out of the exercise table in exercise controller and store the relation in the workout_exercises table
This functin is triggered when creating a workout
Display all exercise based on a workout Id workout controller, function to pick 4 random exercises

### 13/03 Mon
Update workout function: make sure that user can not change the workout name to an existing name, 
Start documentation
### 14/03 Tue
Introduced new table Exercise_filter. The Idea was to filter exercises by level and body region and store the result in this table, than choose 4 random exercises for the training out of that selection.
It looks like it is session.bulk_insert_mappings(MyTable, rows_to_insert) but I could not make it work, kept getting "no such property" error. 
In the end I solved the problem by drawing a random exercise first and than checking if it matches the criteria. if yes, store the result in workout_exercises if not, draw next exercise and check until  found 4 exercises.
### 15/03 Wed
Tried session.bulk_insert_mappings(MyTable, rows_to_insert) , initialise table on its own but no success. I'll try my_table.delete()

Continue Documentation

### 16/03 Thursday
System overview: List down all routes, test plan, explanation

Test plan: Endpoint,  test data, expected return, result
Implement Exception handling in all functions: wrong or missing key

### 17/03 Friday
Implement exception handling for all functions/Routes
Test,  continue on questions , R1, 2, R4, R5, document endpoints

### 18/03 Saturday
Refine questions  R8, R9, Add entity "Progres"
### 18/03 Sunday
Finish documentation, final touches









