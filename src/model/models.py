from main import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer(), primary_key=True)

    username = db.Column(db.String(), nullable=False, unique=True)
    admin = db.Column(db.Boolean())
    mobile_number = db.Column(db.String())
    email = db.Column(db.String(), unique=True)
    password = db.Column(db.String())
    workouts = db.relationship('Workout', backref='user', cascade="all,delete")


class Workout(db.Model):
    __tablename__ = "workouts"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False, unique=True)
    progres = db.Column(db.String())
    date = db.Column(db.Date())
    rest_time = db.Column(db.String())
    rounds = db.Column(db.String())
    # foreign key
    user_id = db.Column(
        db.Integer(), db.ForeignKey("users.id"), nullable=False
    )
    workout_exercises = db.relationship('Workout_Exercise', backref='workout', cascade="all, delete")
    

class Workout_Exercise(db.Model):
    __tablename__ = "workout_exercises"

    id = db.Column(db.Integer(), primary_key=True)
    date = db.Column(db.Date())
    # two foreign keys
    workout_id = db.Column(db.Integer(), db.ForeignKey("workouts.id"), nullable=False)
    exercise_id = db.Column(db.Integer(), db.ForeignKey("exercises.id"), nullable=False)

    

class Exercise(db.Model):
    __tablename__ = "exercises"

    id = db.Column(db.Integer(), primary_key=True)

    name = db.Column(db.String(), nullable=False, unique=True)
    description = db.Column(db.String())
    interval_time = db.Column(db.String())
    repetitions = db.Column(db.String())
    muscle_group = db.Column(db.String())
    level = db.Column(db.String())
    weight = db.Column(db.String())
    workout_exercises = db.relationship('Workout_Exercise', backref='exercise', cascade="all, delete")
