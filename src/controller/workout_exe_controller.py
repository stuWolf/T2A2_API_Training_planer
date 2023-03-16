from main import db
from flask import Blueprint, abort
from model.models import Workout_Exercise, Workout, Exercise
from schema.schemas import workout_exercise_schema, workout_exercises_schema
from datetime import date
from sqlalchemy import func

workout_exercise = Blueprint('workout_exercises', __name__, url_prefix="/workout_exercises")



# Display all exercise based on workout name

@workout_exercise.get("/<string:workout_name>")
def get_exercises(workout_name):
    
        # test if workout name exists
    workout = Workout.query.filter_by(workout_name=workout_name).first()
    if not workout:
        return abort(400, description=f"The workout { workout_name} does not exist")
     # check if workout has exercises
    work_exercises = Workout_Exercise.query.filter_by(workout_id=workout.id).first()
    if not work_exercises:
        print(" not work_exercises")
        return (f"the workout  { workout_name} has no exercises")

    # list exercises   
    work_exercises = Workout_Exercise.query.filter_by(workout_id=workout.id)
    print(" dump_exercises")
    return workout_exercises_schema.dump(work_exercises)
    

# print workout_exercise of one id
@workout_exercise.get("/<int:id>")
def get_workout_exercise(id):
    workout_exercise = Workout_Exercise.query.get(id)

    if not workout_exercise:
        return ("record does not exist" )

    return workout_exercise_schema.dump(workout_exercise)


#pick 4 exercises based on creterias muscle group and level and store them in workout_exercise table
# Create 4 new workout_exercise entries
def pick_exercises(workout_id, body_region, level):

    # no body_region or level specified  
    if not (body_region or level):
        for i in range (4):
        #pick 4 exercises and store them in workout_exercise table
            exercise = Exercise.query.order_by(func.random()).limit(1).one()
        # write a new row into workout_exercises after each iteration
            add_workout_exercise_row(workout_id,exercise.id)
           
        return ("muscle group and level are mixed")
    # body region specified but not level
    if body_region and not level:
        i = 0
   
        # get all exercises of muscle group
        exercises = Exercise.query.filter_by(body_region=body_region).first()

        if exercises:
            # if exersices of the muscle group exists, select first exercise

            
            while i < 4:
            #pick 4 exercises fr<om filtered exercises and store them in workout_exercise table
                exercise = Exercise.query.order_by(func.random()).limit(1).one()
                if exercise.body_region == body_region:
                    i +=1
                    # write exercise in workout exercise table
                    add_workout_exercise_row(workout_id,exercise.id)
                else:
                    pass
            return (f"workout created for the body region { body_region}, level is mixed")
        else:
            return (f"exercises for the body region { body_region} have not been created yet")
        # level specified but nit body region
    if not body_region and level:
        i = 0
   
        # get all exercises of muscle group
        exercises = Exercise.query.filter_by(level=level).first()

        if exercises:
            # if exersices of the muscle group exists, select first exercise
        # store exercises in Exercise filter table
            
            while i < 4:
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
        
    # both specified
    if body_region and level:
        i = 0
   
        # get all exercises of muscle group
        exercises = Exercise.query.filter_by(level=level).filter_by(body_region = body_region ).first()

        if exercises:
            # if exersices of the muscle group exists, select first exercise
        # store exercises in Exercise filter table
            
            while i < 4:
            #pick 4 exercises fr<om filtered exercises and store them in workout_exercise table
                exercise = Exercise.query.order_by(func.random()).limit(1).one()
                if exercise.level == level and exercise.body_region == body_region :
                    i +=1
                    # store exercise in workout exercise table
                    add_workout_exercise_row(workout_id,exercise.id)
                else:
                    pass
            return (f" workout created with level {level} and muscle group {body_region}")
        else:
            return (f"exercises with  the combination {body_region} and {level} have not been created yet")


# write result in workout exercise table
def add_workout_exercise_row(workout_id,exercise_id):
    # createn new object (row)
    workout_exercise = Workout_Exercise()
    workout_exercise.date = date.today()
    workout_exercise.workout_id = workout_id
    workout_exercise.exercise_id = exercise_id
    db.session.add(workout_exercise)
    db.session.commit()


# Test Function :Create 4 new workout_exercise entries, exercise random, a valid workout id is
#  required as secondary key
@workout_exercise.post("/<int:workout_id>")
def create_workout_exercise(workout_id):
    # user_id = get_jwt_identity()
    # user = User.query.get(user_id)
    
    
    workout = Workout.query.get(workout_id)
    if not workout:
        return abort(401, description=f"a workout with the id {workout_id} does not exist")
        
    for i in range (4):
        exercise = Exercise.query.order_by(func.random()).limit(1).one()
        
  
   # write result in workout exercise table
        add_workout_exercise_row(workout_id,exercise.id)
       
    
    return workout_exercise_schema.dump(workout_exercise)


# Delete workout_exercise (only admin or user who created it)
# - not needed as will be deleted automatically with the workout

