from main import db, bcrypt
from flask import Blueprint, request, abort, jsonify
from model.models import Workout, User
from schema.schemas import workout_schema, workouts_schema
from flask_jwt_extended import  jwt_required, get_jwt_identity



workout = Blueprint('workouts', __name__, url_prefix="/workouts")

# create workout

# Ammend and delete workout (only admin or user who created workout)

# print all workouts
@workout.get("/")
def get_workouts():
    workouts = Workout.query.all()
    return workouts_schema.dump(workouts)

# print workout by id
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
        
    workout.user_id = user_id
    workout = Workout(**workout_fields)
    
    db.session.add(workout)
    db.session.commit()
        #create a variable that sets an expiry date
        # expiry = timedelta(days=1)
        #create the access token
        # access_token = create_access_token(identity=str(user.id), expires_delta=expiry)
    # except:
    #     return { "message": "Your information is incorrect" }
    
    return workout_schema.dump(workout)


# Delete workout (admin or user can delete himself )

@workout.delete("/<string:email>")
@jwt_required()
def delete_workout(email):
    #get the operator id invoking get_jwt_identity and find it in the DB
    user_id = get_jwt_identity()
    operator = Workout.query.get(user_id)
    #Make sure operator is in the database
    if not operator:
        return abort(401, description="Invalid operator")
    # Stop the request if the user is not an admin
    if not operator.admin:
        return abort(401, description="You need admin rights for this operation")
    # find the card
    workout = Workout.query.filter_by(email=email).first()
    #return an error if the card doesn't exist
    if not workout:
        return abort(400, description= f"workout {email} does not exist")
    
    #Delete the card from the database and commit
    db.session.delete(workout)
    db.session.commit()
    #return the card in the response
    return jsonify({"user":user.email, "workout_id": workout.id, '_comment': "deleted:"})

# Amend workout (only by the user itself)

@workout.put("/update")
@jwt_required()
def update_workout():

    user_id = get_jwt_identity()
    operator = Workout.query.get(user_id)
    #Make sure operator is in the database
    if not operator:
        return abort(401, description=f"Invalid operator {user_id}")
    else:
              #find the workout
        workout = Workout.query.filter_by(id=workout_id).first()


    # load workout fields from json
    workout_fields = workout_schema.load(request.json)
    email=user_fields["email"]
    # tests if email already exists in any user except the une logged in
    user_any = Workout.query.filter_by(email=email).first()

    if user_any and not user.email == email:
        # return an abort message to inform the user. That will end the request
        return abort(400, description=f"Email {email } already registered")
      #find the user


    
    if not user.admin == True:
        user.admin = False  # false by default, not every user can be admin

    # if user:
    #     # return an abort message to inform the user. That will end the request
    #     return abort(400, description="Email already registered")
# update user record
    # user = User(**user_fields)
    workout.id = workout_id  # keep old workout id
    workout.workoutname = workout_fields["workoutname"]
    workout.mobile_number = workout_fields["mobile_number"]
    workout.email = email
    workout.password = bcrypt.generate_password_hash(workout_fields["password"]).decode("utf-8")
        #Add it to the database and commit the changes
    

    db.session.commit()
    return jsonify({"user":user.email, "usename": user.username, "user_id": user.id, '_comment': "updated:"})
    



# Login


# create workout

# Ammend and delete workout (only admin or user who created workout)

# create, ammend and delete exercise (admin only)


# Create workout exercise ( randomly choose 4 exercises from exercises list)

# print out all exercises of a workout id
# fetch all exercises of under a workout id number from Workout_exercises 
# look up exercises for each exercise id and print them out