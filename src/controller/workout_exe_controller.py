from main import db, bcrypt
from flask import Blueprint, request, abort, jsonify
from model.models import Workout_Exercise, Workout, Exercise, Exercise_filter
from schema.schemas import workout_exercise_schema, workout_exercises_schema
from flask_jwt_extended import  jwt_required, get_jwt_identity
from datetime import date
from sqlalchemy import func

workout_exercise = Blueprint('workout_exercises', __name__, url_prefix="/workout_exercises")

# Create workout exercise ( randomly choose 4 exercises from exercises list)

# print out all exercises of a workout id
# fetch all exercises of under a workout id number from Workout_exercises 
# look up exercises for each exercise id and print them out

# print all workout_exercises
# @workout_exercise.get("/")
# def get_workout_exercises():
#     workout_exercises = Workout_Exercise.query.all()
#     return workout_exercises_schema.dump(workout_exercises)

# Display all exercise based on workout ID
# change to workout name !
@workout_exercise.get("/<int:workout_id>")
def get_exercises(workout_id):
    # exercises = Exercise.query.all()
    workout_exercises = Workout_Exercise.query.filter_by(workout_id=workout_id)
    return workout_exercises_schema.dump(workout_exercises)

# print workout_exercise of one id
@workout_exercise.get("/<int:id>")
def get_workout_exercise(id):
    workout_exercise = Workout_Exercise.query.get(id)

    if not workout_exercise:
        return { "message": "Don't try to hack me" }

    return workout_exercise_schema.dump(workout_exercise)


#pick 4 exercises based on creterias muscle group and level and store them in workout_exercise table
# Create 4 new workout_exercise
def pick_exercises(workout_id, muscle_group, level):
# if muscle_group or level are not null, the exercises need to be filtered and stored in 
# an own table first. Than the program can pick random exercises from the filtered table
# the output of query itself is not colatable
    if not (muscle_group or level):
        for i in range (4):
        #pick 4 exercises and store them in workout_exercise table
            exercise = Exercise.query.order_by(func.random()).limit(1).one()
        # exercise_id = exercise.id
            add_workout_exercise_row(workout_id,exercise.id)
           
        return ("muscle group and level are mixed")

    if muscle_group and not level:
        filter_exercises = Exercise_filter()
        # get all exercises of muscle group
        filter_exercises = Exercise.query.filter_by(muscle_group=muscle_group)
        # store exercises in Exercise filter table
        db.session.add(filter_exercises)
        db.session.commit()
        for i in range (4):
        #pick 4 exercises from filtered exercises and store them in workout_exercise table
            exercise = Exercise_filter.query.order_by(func.random()).limit(1).one()
        # write exercise in workout exercise table
            add_workout_exercise_row(workout_id,exercise.id)
        return ("level is mixed")
    
    if not muscle_group and level:

        return ("muscle_group is mixed")

# write exercise in workout exercise table
def add_workout_exercise_row(workout_id,exercise_id):
    
    workout_exercise = Workout_Exercise()
    workout_exercise.date = date.today()
    workout_exercise.workout_id = workout_id
    workout_exercise.exercise_id = exercise_id
    db.session.add(workout_exercise)
    db.session.commit()


# Help Function :Create 4 new workout_exercise 
@workout_exercise.post("/<int:workout_id>")
def create_workout_exercise(workout_id):
    # user_id = get_jwt_identity()
    # user = User.query.get(user_id)
    
    
    workout = Workout.query.get(workout_id)
    if not workout:
        return abort(401, description=f"a workout with the id {workout_id} does not exist")
        
    for i in range (4):
        exercise = Exercise.query.order_by(func.random()).limit(1).one()
        exercise_id = exercise.id
    # try:
    # workout_exercise_fields = workout_exercise_schema.load(request.json)
         # find the workout_exercise
    # exercise = Exercise.query.limit(1)
    # creatennew object
        workout_exercise = Workout_Exercise()
        workout_exercise.date = date.today()
        workout_exercise.workout_id = workout_id
        workout_exercise.exercise_id = exercise_id
        db.session.add(workout_exercise)
        db.session.commit()
       
    
    return workout_exercise_schema.dump(workout_exercise)


# Delete workout_exercise (only admin or user who created it )
# not needed as will be deleted automatically with the workout

