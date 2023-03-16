from main import db
from flask import Blueprint, request, abort, jsonify
from datetime import date
from model.models import Workout, User
from schema.schemas import workout_schema, workouts_schema
from controller.workout_exe_controller import pick_exercises
from flask_jwt_extended import  jwt_required, get_jwt_identity



workout = Blueprint('workouts', __name__, url_prefix="/workouts")



# print all workouts of logged in user
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
        return{"message": f"A workout with id { id } doesn't exist"  }

    return workout_schema.dump(workout)


# Create new workout with the user id of logged in user
@workout.post("/")
@jwt_required()
def create_workout():
    user_id = get_jwt_identity()

    # load workout fields from json
    workout_fields = workout_schema.load(request.json)
    # test if workout name is provided
    workout_name = workout_fields["workout_name"]
    if not workout_name:
         return abort(400, description=f"The workout needs a name")
    # test if workout name is provided
    workout = Workout.query.filter_by(workout_name=workout_name).first()
    if workout:
        return abort(400, description=f"A workout with the name {workout_name} already exists")
    # create new workout object
    workout = Workout(**workout_fields)
    workout.date = date.today()
    workout.user_id = user_id

    db.session.add(workout)
    db.session.commit()
    #pick 4 exercises based on creterias muscle group and level and store them in workout_exercise table
    result = pick_exercises(workout.id, workout.body_region, workout.level)
    print(result)
    return workout_schema.dump(workout)


# Delete workout (only admin or user who created it can delete )

@workout.delete("/<string:workout_name>")
@jwt_required()
def delete_workout(workout_name):
    #get the operator id invoking get_jwt_identity and find it in the DB
    user_id = int(get_jwt_identity())
    # get whole user record
    user = User.query.get(user_id)

    workout = Workout.query.get(user_id)
    #Test if workouts under the name of operator exist
    if not workout:
        return abort(401, description="you have no workouts created yet")
    #Test if workouts with this id exist
# get the workout
    workout = Workout.query.filter_by(workout_name=workout_name).first()
    if not workout:
        return abort(401, description=f"a workout with the id { workout_name} does not exist")
    
    # Stop the request if the user is not an admin or tries to edit someone elses card
    if not (user.admin or  (user_id == workout.user_id)):
        return abort(401, description="You can only edit your own workouts or need to be an admin")
   
    
    #Delete the workout from the database and commit
    db.session.delete(workout)
    db.session.commit()
    #return the workout in the response
    return jsonify({"workout_user":workout.user_id, "workout_name": workout.workout_name, '_comment': "deleted:"})

# Amend workout (only user who created it)

@workout.put("/update/<string:workout_name>")
@jwt_required()
def update_workout(workout_name):
   
   #get the operator id invoking get_jwt_identity and find it in the DB
    user_id = int(get_jwt_identity())
    user = User.query.get(user_id)
    # find the workout, test if it exists
   
    workout = Workout.query.get(user_id)
    #Test if workouts under the name of operator exist
    if not workout:
        return abort(401, description="you have no workouts created yet")
   
    # Stop the request if the user is not an admin or tries to edit someone elses card
    if not (user.admin or  (user_id == workout.user_id)):
        return abort(401, description="You can only edit your own workouts or need to be an admin")

     # get the workout
   
    workout_old = Workout.query.filter_by(workout_name=workout_name).first()
    if not workout_old:
        return abort(401, description=f"a workout with the name '{workout_name}' does not exist")
    # load workout fields from json
    workout_fields = workout_schema.load(request.json)
    new_name = workout_fields["workout_name"]
# if a workout with the new name exists and the current workout has not 
    # check if any workout except the current one has that workout_name
    workout = Workout.query.filter_by(workout_name=new_name).first()
    if workout and not (workout_old.workout_name == new_name):
    # if  not workout_old.name == workout_name:
        return abort(400, description=f"you nan not use the name '{new_name}',it already exists")
    
    # finally update workout
    workout = Workout.query.filter_by(workout_name=workout_name).first()
    # here first() is OK because workout name is unique
    workout.workout_name = new_name
    workout.rest_time = workout_fields["rest_time"]
    workout.rounds = workout_fields["rounds"]
    workout.body_region = workout_fields["body_region"]
    workout.level = workout_fields["level"]
    workout.progres = workout_fields["progres"]
    
    workout.date = date.today()

    # db.session.add(workout) ??
    db.session.commit()
    # return jsonify({"user":user.email, "workout_name": workout.name, "workout_id": workout.id, '_comment': "updated:"})
    return workout_schema.dump(workout)



