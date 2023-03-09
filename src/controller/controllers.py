from flask import Blueprint, request

from model.models import User, Workout, Workout_Exercise, Exercise
from schema.schemas import user_schema,users_schema, workout_schema, workouts_schema, workout_exercises_schema, workout_exercise_schema, exercise_schema, exercises_schema

from main import db

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


# Create User
@user.post("/")
def create_user():
    try:
        user_fields = user_schema.load(request.json)
        user = User(**user_fields)

        db.session.add(user)
        db.session.commit()
    except:
        return { "message": "Your information is incorrect" }

    return user_schema.dump(user)


# Delete User (admin only)

# Amend User

# Login



# create workout

# Ammend and delete workout (only admin or user who created workout)

# create, ammend and delete exercise (admin only)


# Create workout exercise ( randomly choose 4 exercises from exercises list)

# print out all exercises of a workout id
# fetch all exercises of under a workout id number from Workout_exercises 
# look up exercises for each exercise id and print them out