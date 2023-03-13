from main import db
from flask import Blueprint, request, abort, jsonify
from datetime import date
from model.models import Workout, User
from schema.schemas import workout_schema, workouts_schema
from flask_jwt_extended import  jwt_required, get_jwt_identity



workout = Blueprint('workouts', __name__, url_prefix="/workouts")

# create workout

# Ammend and delete workout (only admin or user who created workout)

# print all workouts for the logged in user
@workout.get("/")

def get_workouts():
    
    workouts = Workout.query.all()
    return workouts_schema.dump(workouts)


# print all workouts of a certain user

# print workout of a speific id
@workout.get("/<int:id>")
def get_workout(id):
    workout = Workout.query.get(id)

    if not workout:
        return { "message": "A workout with that id doesn't exist"  }

    return workout_schema.dump(workout)


# Register new workout
@workout.post("/")
@jwt_required()
def create_workout():
    user_id = get_jwt_identity()
    # user = User.query.get(user_id)

    workout_fields = workout_schema.load(request.json)
    # create workout object
    workout = Workout(**workout_fields)
    workout.date = date.today()
    workout.user_id = user_id
    db.session.add(workout)
    db.session.commit()
       
    
    return workout_schema.dump(workout)


# Delete workout (only admin or user who created it can delete )

@workout.delete("/<int:id>")
@jwt_required()
def delete_workout(id):
    #get the operator id invoking get_jwt_identity and find it in the DB
    user_id = int(get_jwt_identity())
    user = User.query.get(user_id)
    
    #Test if workouts with this id exist

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
   
    
    #return an error if the card doesn't exist
    # if not workout:
    #     return abort(400, description= f"workout {email} does not exist")
    
    #Delete the card from the database and commit
    db.session.delete(workout)
    db.session.commit()
    #return the workout in the response
    return jsonify({"workout_user":workout.user_id, "logedin_user": user_id, "workout_id": workout.id, '_comment': "deleted:"})

# Amend workout (only by the user itself)

@workout.put("/update/<int:id>")
@jwt_required()
def update_workout(id):
   
   #get the operator id invoking get_jwt_identity and find it in the DB
    user_id = int(get_jwt_identity())
    user = User.query.get(user_id)
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
    # name=workout_fields["name"]
     # find the workout, test if it exists
    workout = Workout.query.filter_by(id=id).first()
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
    workout.date = date.today()
    workout.name = workout_fields["name"]
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