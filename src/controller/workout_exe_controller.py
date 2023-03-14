from main import db
from flask import Blueprint, abort
from model.models import Workout_Exercise, Workout, Exercise
from schema.schemas import workout_exercise_schema, workout_exercises_schema
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
@workout_exercise.get("/<string:workout_name>")
def get_exercises(workout_name):
    # exercises = Exercise.query.all()
    workout = Workout.query.filter_by(workout_name=workout_name).first()
    workout_exercises = Workout_Exercise.query.filter_by(workout_id=workout.id)
    return workout_exercises_schema.dump(workout_exercises)

# print workout_exercise of one id
@workout_exercise.get("/<int:id>")
def get_workout_exercise(id):
    workout_exercise = Workout_Exercise.query.get(id)

    if not workout_exercise:
        return {"reckord does not exist" }

    return workout_exercise_schema.dump(workout_exercise)


#pick 4 exercises based on creterias muscle group and level and store them in workout_exercise table
# Create 4 new workout_exercise
def pick_exercises(workout_id, body_region, level):
# if body_region or level are not null, the exercises need to be filtered and stored in 
# an own table first. Than the program can pick random exercises from the filtered table
# the output of query itself is not colatable

    # no body_region or level,  
    if not (body_region or level):
        for i in range (4):
        #pick 4 exercises and store them in workout_exercise table
            exercise = Exercise.query.order_by(func.random()).limit(1).one()
        # write a new row into workout_exercises after each iteration
            add_workout_exercise_row(workout_id,exercise.id)
           
        return ("muscle group and level are mixed")

    if body_region and not level:
        i = 0
   
        # get all exercises of muscle group
        exercises = Exercise.query.filter_by(body_region=body_region).first()

        if exercises:
            # if exersices of the muscle group exists, select first exercise
        # store exercises in Exercise filter table
            
            while i <= 3:
            #pick 4 exercises fr<om filtered exercises and store them in workout_exercise table
                exercise = Exercise.query.order_by(func.random()).limit(1).one()
                if exercise.body_region == body_region:
                    i +=1
                    # write exercise in workout exercise table
                    add_workout_exercise_row(workout_id,exercise.id)
                else:
                    pass
            return (f"workout created for the body region {body_region}, level is mixed")
        else:
            return (f"exercises for the body region {body_region} have not been created yet")
    if not body_region and level:
        i = 0
   
        # get all exercises of muscle group
        exercises = Exercise.query.filter_by(level=level).first()

        if exercises:
            # if exersices of the muscle group exists, select first exercise
        # store exercises in Exercise filter table
            
            while i <= 3:
            #pick 4 exercises fr<om filtered exercises and store them in workout_exercise table
                exercise = Exercise.query.order_by(func.random()).limit(1).one()
                if exercise.level == level:
                    i +=1
                    # write exercise in workout exercise table
                    add_workout_exercise_row(workout_id,exercise.id)
                else:
                    pass
            return (f" workout created with level {level} body_region is mixed")
        else:
            return (f"exercises for the level {level} have not been created yet")
        

    if body_region and level:
        i = 0
   
        # get all exercises of muscle group
        exercises = Exercise.query.filter_by(level=level).filter_by(body_region = body_region ).first()

        if exercises:
            # if exersices of the muscle group exists, select first exercise
        # store exercises in Exercise filter table
            
            while i <= 3:
            #pick 4 exercises fr<om filtered exercises and store them in workout_exercise table
                exercise = Exercise.query.order_by(func.random()).limit(1).one()
                if exercise.level == level and exercise.body_region == body_region :
                    i +=1
                    # write exercise in workout exercise table
                    add_workout_exercise_row(workout_id,exercise.id)
                else:
                    pass
            return (f" workout created with level {level} and muscle group {body_region}")
        else:
            return (f"exercises with  the combination {body_region} and {level} have not been created yet")


# write exercise in workout exercise table
def add_workout_exercise_row(workout_id,exercise_id):
    
    workout_exercise = Workout_Exercise()
    workout_exercise.date = date.today()
    workout_exercise.workout_id = workout_id
    workout_exercise.exercise_id = exercise_id
    db.session.add(workout_exercise)
    db.session.commit()


# Test Function :Create 4 new workout_exercise 
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

