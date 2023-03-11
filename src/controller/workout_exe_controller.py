from main import db, bcrypt
from flask import Blueprint, request, abort, jsonify
from model.models import Workout_Exercise, User, Workout, Exercise
from schema.schemas import workout_exercise_schema, workout_exercises_schema
from flask_jwt_extended import  jwt_required, get_jwt_identity
from datetime import date


workout_exercise = Blueprint('workout_exercises', __name__, url_prefix="/workout_exercises")

# Create workout exercise ( randomly choose 4 exercises from exercises list)

# print out all exercises of a workout id
# fetch all exercises of under a workout id number from Workout_exercises 
# look up exercises for each exercise id and print them out

# print all workout_exercises
@workout_exercise.get("/")
def get_workout_exercises():
    workout_exercises = Workout_Exercise.query.all()
    return workout_exercises_schema.dump(workout_exercises)

# print workout_exercise by id
@workout_exercise.get("/<int:id>")
def get_workout_exercise(id):
    workout_exercise = Workout_Exercise.query.get(id)

    if not workout_exercise:
        return { "message": "Don't try to hack me" }

    return workout_exercise_schema.dump(workout_exercise)


# Create new workout_exercise
@workout_exercise.post("/<int:workout_id>")
def create_workout_exercise(workout_id):
    # user_id = get_jwt_identity()
    # user = User.query.get(user_id)
    
 
    
    workout = Workout.query.get(workout_id)
    if not workout:
        return abort(401, description=f"a workout with the id {workout_id} does not exist")

    # try:
    # workout_exercise_fields = workout_exercise_schema.load(request.json)
         # find the workout_exercise
    # exercise = Exercise.query.limit(1)
    # exercise_id = exercise.id
    workout_exercise = Workout_Exercise
    workout_exercise.date = date.today()
    workout_exercise.workout_id = workout_id
    workout_exercise.exercise_id = exercise_id
    db.session.add(workout_exercise)
    db.session.commit()
        #create a variable that sets an expiry date
        # expiry = timedelta(days=1)
        #create the access token
        # access_token = create_access_token(identity=str(user.id), expires_delta=expiry)
    # except:
    #     return { "message": "Your information is incorrect" }
    
    return workout_exercise_schema.dump(workout_exercise)


# Delete workout_exercise (admin or user can delete himself )

@workout_exercise.delete("/<string:email>")
@jwt_required()
def delete_workout_exercise(email):
    #get the operator id invoking get_jwt_identity and find it in the DB
    user_id = get_jwt_identity()
    operator = Workout_Exercise.query.get(user_id)
    #Make sure operator is in the database
    if not operator:
        return abort(401, description="Invalid operator")
    # Stop the request if the user is not an admin
    if not operator.admin:
        return abort(401, description="You need admin rights for this operation")
    # find the card
    workout_exercise = Workout_Exercise.query.filter_by(email=email).first()
    #return an error if the card doesn't exist
    if not workout_exercise:
        return abort(400, description= f"workout_exercise {email} does not exist")
    
    #Delete the card from the database and commit
    db.session.delete(workout_exercise)
    db.session.commit()
    #return the card in the response
    return jsonify({"user":user.email, "workout_exercise_id": workout_exercise.id, '_comment': "deleted:"})

# Amend workout_exercise (only by the user itself)

@workout_exercise.put("/update")
@jwt_required()
def update_workout_exercise():

    user_id = get_jwt_identity()
    operator = Workout_Exercise.query.get(user_id)
    #Make sure operator is in the database
    if not operator:
        return abort(401, description=f"Invalid operator {user_id}")
    else:
              #find the workout
        workout_exercise = Workout_Exercise.query.filter_by(id=workout_exercise_id).first()


    # load workout fields from json
    workout_exercise_fields = workout_exercise_schema.load(request.json)
    email=user_fields["email"]
    # tests if email already exists in any user except the une logged in
    user_any = Workout_Exercise.query.filter_by(email=email).first()

 


    
   

    # if user:
    #     # return an abort message to inform the user. That will end the request
    #     return abort(400, description="Email already registered")
# update user record
    # user = User(**user_fields)
    workout_exercise.workout_id = workout_id  # keep old workout_exercise id
    workout_exercise.workout_exercisename = workout_exercise_fields["workout_exercisename"]
    workout_exercise.mobile_number = workout_exercise_fields["mobile_number"]
    workout_exercise.email = email
    workout_exercise.password = bcrypt.generate_password_hash(workout_exercise_fields["password"]).decode("utf-8")
        #Add it to the database and commit the changes
    

    db.session.commit()
    return jsonify({"user":user.email, "usename": user.username, "user_id": user.id, '_comment': "updated:"})
    



# Login




# create, ammend and delete exercise (admin only)


# Create workout exercise ( randomly choose 4 exercises from exercises list)

# print out all exercises of a workout id
# fetch all exercises of under a workout id number from Workout_exercises 
# look up exercises for each exercise id and print them out