from main import db
from flask import Blueprint, request, abort, jsonify
from datetime import date
from model.models import Workout, User
from schema.schemas import workout_schema, workouts_schema
from controller.workout_exe_controller import pick_exercises
from flask_jwt_extended import  jwt_required, get_jwt_identity



workout = Blueprint('workouts', __name__, url_prefix="/workouts")

# create workout

# Ammend and delete workout (only admin or user who created workout)

# print all workouts of logged in userR
@workout.get("/")
@jwt_required()
def get_workouts():
    user_id = get_jwt_identity()
    workouts = Workout.query.filter_by(user_id=user_id).all()
    


    
    return workouts_schema.dump(workouts)


# print all workouts of a certain user

# print workout of a speific id
@workout.get("/<int:id>")
def get_workout(id):
    workout = Workout.query.get(id)

    if not workout:
        return { "message": "A workout with that id doesn't exist"  }

    return workout_schema.dump(workout)


# Create new workout
@workout.post("/")
@jwt_required()
def create_workout():
    user_id = get_jwt_identity()
    # user = User.query.get(user_id)


    # load workout fields from json
    workout_fields = workout_schema.load(request.json)
    workout_name = workout_fields["workout_name"]
    if not workout_name
         return abort(400, description=f"The workout needs a name")
    print(workout_name)
    workout = Workout.query.filter_by(workout_name=workout_name).first()
    if workout:
        return abort(400, description=f"A workout with the name {workout_name} already exists")
    # create ew workout object
    workout = Workout(**workout_fields)
    workout.date = date.today()
    workout.user_id = user_id
    # print(name)
    db.session.add(workout)
    db.session.commit()
    #pick 4 exercises based on creterias muscle group and level and store them in workout_exercise table
    result = pick_exercises(workout.id, workout.muscle_group, workout.level)
    print(f"workout created with {workout.muscle_group, workout.level} and {result}")
    return workout_schema.dump(workout)


# Delete workout (only admin or user who created it can delete )

@workout.delete("/<string:workout_name>")
@jwt_required()
def delete_workout(workout_name):
    #get the operator id invoking get_jwt_identity and find it in the DB
    user_id = int(get_jwt_identity())
    user = User.query.get(user_id)

    workout = Workout.query.get(user_id)
    #Test if workouts under the name of operator exist
    if not workout:
        return abort(401, description="you have no workouts created yet")
    #Test if workouts with this id exist
# get the workout
    workout = Workout.query.filter_by(workout_name=workout_name).first()
    if not workout:
        return abort(401, description=f"a workout with the id {workout_name} does not exist")
    
    # Stop the request if the user is not an admin or tries to edit someone elses card
    if not (user.admin or  (user_id == workout.user_id)):
        return abort(401, description="You can only edit your own workouts or need to be an admin")
   
    
    #return an error if the card doesn't exist
    # if not workout:
    #     return abort(400, description= f"workout {email} does not exist")
    
    #Delete the card from the database and commit
    db.session.delete(workout)
    db.session.commit()
    #return the workout in the response
    return jsonify({"workout_user":workout.user_id, "workout_name": workout.workout_name, '_comment': "deleted:"})

# Amend workout (only user who created it)

@workout.put("/update/<int:id>")
@jwt_required()
def update_workout(id):
   
   #get the operator id invoking get_jwt_identity and find it in the DB
    user_id = int(get_jwt_identity())
    user = User.query.get(user_id)
    # find the workout, test if it exists
    workout = Workout.query.get(id)
    if not workout:
        return abort(401, description=f"a workout with the id {id} does not exist")

    workout = Workout.query.get(user_id)
    #Test if workouts under the name of operator exist
    if not workout:
        return abort(401, description="you have no workouts created yet")
    # get the workout
    workout = Workout.query.filter_by(id=id).first()
    # Stop the request if the user is not an admin or tries to edit someone elses card
    if not (user.admin or  (user_id == workout.user_id)):
        return abort(401, description="You can only edit your own workouts or need to be an admin")


    # load workout fields from json
    workout_fields = workout_schema.load(request.json)
    new_name = workout_fields["workout_name"]

    # check if any workout except the current one has that workout_name
    workout = Workout.query.filter_by(workout_name=new_name).first()
    if workout:
        return abort(400, description=f"A workout with the name {new_name} already exists")
    # workout = Workout.query.filter_by(name=name).first()
    # if workout:
        
    #     return abort(400, description=f"A workout with the workout_name {workout_name} already exists")
    # name=workout_fields["name"]
     

    # exercise = Exercise.query.get(name) # argument needs to be int, so id only
    # if not workout:
    #     # return an abort message to inform the exercise. That will end the request
    #     return abort(400, description=f"An workout with the name {name} does not exist")
    # old_id = workout.id
    # user_id = workout.user_id
    # create new object with updated exercise filds
    # workout = Workout(**workout_fields)
    # workout.id = old_id # keep old exercise id
    # workout.user_id = user_id
    # finally update workout
    workout.date = date.today()
    workout.workout_name = new_name
    workout.progres = workout_fields["progres"]
    workout.rest_time = workout_fields["rest_time"]
    workout.rounds = workout_fields["rounds"]
    

    # db.session.add(workout)
    db.session.commit()
    # return jsonify({"user":user.email, "workout_name": workout.name, "workout_id": workout.id, '_comment': "updated:"})
    return workout_schema.dump(workout)



# Login


# create workout

# Ammend and delete workout (only admin or user who created workout)

# create, ammend and delete exercise (admin only)


# Create workout exercise ( randomly choose 4 exercises from exercises list)

# print out all exercises of a workout id
# fetch all exercises of under a workout id number from Workout_exercises 
# look up exercises for each exercise id and print them out