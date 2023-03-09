from main import db, bcrypt
from flask import Blueprint, request, abort, jsonify
from datetime import timedelta
import os
from model.models import User, Workout, Workout_Exercise, Exercise
from schema.schemas import user_schema,users_schema, workout_schema, workouts_schema, workout_exercises_schema, workout_exercise_schema, exercise_schema, exercises_schema
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity



user = Blueprint('users', __name__, url_prefix="/users")



# print all users
@user.get("/")
def get_users():
    users = User.query.all()
    return users_schema.dump(users)

# print user by id
@user.get("/<int:id>")
def get_user(id):
    user = User.query.get(id)

    if not user:
        return { "message": "Don't try to hack me" }

    return user_schema.dump(user)


# Register new User
@user.post("/")
def create_user():
    # try:
    user_fields = user_schema.load(request.json)
         # find the user
    user = User.query.filter_by(email=user_fields["email"]).first()

    if user:
        # return an abort message to inform the user. That will end the request
        return abort(400, description="Email already registered")

        


    user = User(**user_fields)
    user.password = bcrypt.generate_password_hash(user_fields["password"]).decode("utf-8")
        #Add it to the database and commit the changes
    user.admin = False  # false by default, not every user can be admin

    db.session.add(user)
    db.session.commit()
        #create a variable that sets an expiry date
        # expiry = timedelta(days=1)
        #create the access token
        # access_token = create_access_token(identity=str(user.id), expires_delta=expiry)
    # except:
    #     return { "message": "Your information is incorrect" }
    


    return user_schema.dump(user)


# Delete User (admin only)

# Amend User

# Login

@user.post("/login")
def auth_login():
    #get the user data from the request
    user_fields = user_schema.load(request.json)
    #find the user in the database by email
    user = User.query.filter_by(email=user_fields["email"]).first()
    # there is not a user with that email or if the password is no correct send an error
    if not user or not bcrypt.check_password_hash(user.password, user_fields["password"]):
        return abort(401, description="Incorrect username and password")
    
    # return jsonify(message='Login suceeded'), 200
    
    #create a variable that sets an expiry date
    expiry = timedelta(days=1)
    #create the access token
    access_token = create_access_token(identity=str(user.id), expires_delta=expiry)
    # return the user email and the access token
    return jsonify({"user":user.email, "token": access_token, "user_id": user.id })



# create workout

# Ammend and delete workout (only admin or user who created workout)

# create, ammend and delete exercise (admin only)


# Create workout exercise ( randomly choose 4 exercises from exercises list)

# print out all exercises of a workout id
# fetch all exercises of under a workout id number from Workout_exercises 
# look up exercises for each exercise id and print them out