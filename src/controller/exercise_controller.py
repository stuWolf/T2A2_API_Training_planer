from main import db
from flask import Blueprint, request, abort, jsonify
from model.models import  Exercise, User
from schema.schemas import  exercise_schema, exercises_schema
from flask_jwt_extended import  jwt_required, get_jwt_identity



exercise = Blueprint('exercises', __name__, url_prefix="/exercises")

# create, ammend and delete exercise (admin only)

# print all ecercises
@exercise.get("/")
def get_exercises():
    exercises = Exercise.query.all()
    return exercises_schema.dump(exercises)


# print all exercises for a body region
@exercise.get("/<string:body_region>")
def get_nr_exercises(body_region):
    # test if any exercises for the input regin exist
    exercises = Exercise.query.filter_by(body_region=body_region).first()

    if not exercises:
        
        return abort(400, description=f"Exercises for { body_region} have not been created yet.")
 
    exercises = Exercise.query.filter_by(body_region=body_region)
    return exercises_schema.dump(exercises)



# Create new exercise (admin only)
@exercise.post("/")
@jwt_required()
def create_exercise():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    
    if not user.admin:
        return abort(401, description="You need admin rights for this operation")
    
    exercise_fields = exercise_schema.load(request.json)
    name=exercise_fields["name"]
     # find the exercise, test if name already exists
    exercise = Exercise.query.filter_by(name=name).first()
    if exercise:
        
        return abort(400, description=f"An exercise with the name { name} already exists")
    
    exercise = Exercise(**exercise_fields)

    db.session.add(exercise)
    db.session.commit()
        
    
    return exercise_schema.dump(exercise)


# Delete exercise (admin or user can delete himself )

@exercise.delete("/<int:id>")
@jwt_required()
def delete_exercise(id):
    #get the operator id invoking get_jwt_identity and find it in the DB
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    # Stop the request if the user is not an admin
    if not user.admin:
        return abort(401, description="You need admin rights for this operation")
    # load exercise
    exercise = Exercise.query.filter_by(id=id).first()
    #return an error if the card doesn't exist
    if not exercise:
        return abort(400, description= f"Exercise with id { id} does not exist")
    
    #Delete the card from the database and commit
    db.session.delete(exercise)
    db.session.commit()
    #return the card in the response
    return jsonify({"name":exercise.name, "exercise_id": exercise.id, '_comment': "deleted:"})

# Amend exercise (only admin)

@exercise.put("/update")
@jwt_required()
def update_exercise():

    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    # Stop the request if the user is not an admin
    if not user.admin:
        return abort(401, description="You need admin rights for this operation")
    # load user input
    exercise_fields = exercise_schema.load(request.json)
    name=exercise_fields["name"]
     # find the exercise, test if it exists
    exercise = Exercise.query.filter_by(name=name).first()
    # exercise = Exercise.query.get(name) # argument needs to be int, so id only
    if not exercise:
        # return an abort message to inform the exercise. That will end the request
        return abort(400, description=f"An exercise with the name {name} does not exist")
    # update values
    exercise.name = exercise_fields["name"]
    exercise.description = exercise_fields["description"]
    exercise.interval_time = exercise_fields["interval_time"]
    exercise.repetitions = exercise_fields["repetitions"]
    exercise.body_region = exercise_fields["body_region"]
    exercise.level = exercise_fields["level"]
    exercise.weight = exercise_fields["weight"]
    
    db.session.commit()
    return jsonify({"user":user.email, "exercise Name": exercise.name, "exercise_id": exercise.id, "level": exercise.level, '_comment': "updated:"})
    



# Login





# create workout

# Ammend and delete workout (only admin or user who created workout)

# create, ammend and delete exercise (admin only)


# Create workout exercise ( randomly choose 4 exercises from exercises list)

# print out all exercises of a workout id
# fetch all exercises of under a workout id number from Workout_exercises 
# look up exercises for each exercise id and print them out