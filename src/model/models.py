from main import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer(), primary_key=True)

    username = db.Column(db.String(), nullable=False, unique=True)
    verified = db.Column(db.Boolean())
    mobile_number = db.Column(db.String())
    post_code = db.Column(db.String())

class Workout(db.Model):
    __tablename__ = "workouts"

    id = db.Column(db.Integer(), primary_key=True)

    progres = db.Column(db.String(), nullable=False, unique=True)
    date = db.Column(db.Boolean())
    user_id = db.Column(
        db.Integer(), db.ForeignKey("users.id"), nullable=False
    )

    user = db.relationship('User', backref='workouts')

class Workout_Exercise(db.Model):
    __tablename__ = "workout_exercises"

    id = db.Column(db.Integer(), primary_key=True)

    progres = db.Column(db.String(), nullable=False, unique=True)
    date = db.Column(db.Boolean())
    workout_id = db.Column(
        db.Integer(), db.ForeignKey("workouts.id"), nullable=False
    )
    exercise_id = db.Column(
        db.Integer(), db.ForeignKey("exercises.id"), nullable=False
    )

    workout = db.relationship('Workout', backref='workout_exercises')
    exercise = db.relationship('Exercise', backref='workout_exercises')


class Exercise(db.Model):
    __tablename__ = "exercises"

    id = db.Column(db.Integer(), primary_key=True)

    name = db.Column(db.String(), nullable=False, unique=True)
    description = db.Column(db.String())
    interval_time = db.Column(db.String())
    repetitions = db.Column(db.String())
    rest_time = db.Column(db.String())
    rounds = db.Column(db.String())
    muscle_group = db.Column(db.String())
    level = db.Column(db.String())
    
