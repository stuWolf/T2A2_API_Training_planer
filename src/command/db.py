from main import db, bcrypt
from flask import Blueprint
from datetime import date
from model.models import User, Workout, Workout_Exercise, Exercise

db_cmd = Blueprint("db", __name__)

@db_cmd.cli.command('init')
def initialise_db():
    db.drop_all()
    print('Tables are dropped, Nahhh!!')
    db.create_all()
    print('Tables are created, Hoorayy!!')
    db_seed()



@db_cmd.cli.command('create')
def create_db():
    db.create_all()
    print('Tables are created, Hoorayy!!')


@db_cmd.cli.command('drop')
def drop_db():
    db.drop_all()
    print('Tables are dropped, Nahhh!!')


# @db_cmd.cli.command("seed")
def db_seed():
    admin_user = User(
        username = 'The Administrator',
        email = "admin@email.com",
        password = bcrypt.generate_password_hash("password123").decode("utf-8"),
        admin = True,
        # password = "password123",
        mobile_number = "2345235"
    )
    db.session.add(admin_user)

    user1 = User(
        username = 'Arnold Schwarzenegger',
        email = "arni@email.com",
        password = bcrypt.generate_password_hash("p@ssword123").decode("utf-8"),
        admin = False,
        # password = "password123",
        mobile_number = "2345235"
    )
    db.session.add(user1)
    db.session.commit()

    first_workout = Workout(
        progres = '25 min',
        date = date.today(),
        rest_time = "1 min",
        rounds = "5",
               
        user_id = user1.id
    )
    db.session.add(first_workout)

    other_workout = Workout(
        progres = '30 min',
        date = date.today(),
        rest_time = "2 min",
        rounds = "8",
        
        user_id = admin_user.id
    )
    db.session.add(other_workout)


    pull_ups = Exercise(
        name = "Pull Ups",
        description = "deploy core",
        interval_time = "na",
        repetitions = "10",
        muscle_group = "lats, arms",
        level = "hard"

    )
    db.session.add(pull_ups)

    inverted_row = Exercise(
        name = "Inverted Row",
        description = "deploy core",
        interval_time = "na",
        repetitions = "20",
        muscle_group = "back, shoulder",
        level = "meduim"

    )
    db.session.add(inverted_row)

    squat_jumps = Exercise(
        name = "Squat Jumps",
        description = "chest proud",
        interval_time = "na",
        repetitions = "15",
        muscle_group = "glut",
        level = "easy"
    )
    db.session.add(squat_jumps)

    sit_ups = Exercise(
        name = "Sit Ups",
        description = "n.a.",
        interval_time = "1 min",
        repetitions = "Max reps",
        muscle_group = "core",
        level = "easy"
    )
    db.session.add(sit_ups)

    bi_cycle = Exercise(
        name = "Bi Cycle",
        description = "elbows on knees",
        interval_time = "1 min",
        repetitions = "Max reps",
        muscle_group = "core",
        level = "easy"
    )
    db.session.add(bi_cycle )

    push_ups = Exercise(
        name = "Push Ups",
        description = "hold back streight",
        interval_time = "na",
        repetitions = "20",
        muscle_group = "chest",
        level = "medium"

    )
    db.session.add(push_ups)

    Cl_push_ups = Exercise(
        name = "Chest clap Push Ups",
        description = "hold back streight",
        interval_time = "na",
        repetitions = "20",
        muscle_group = "chest",
        level = "medium"

    )
    db.session.add(Cl_push_ups)

    squat_clean = Exercise(
        name = "Squat clean",
        description = "chest proud",
        interval_time = "3 min",
        repetitions = "Max reps",
        muscle_group = "chest",
        level = "medium",
        weight = "2x 8kg"

    )
    db.session.add(squat_clean)
    
    
    db.session.commit()





    work_exercise = Workout_Exercise(
        date = date.today(),
        workout_id = first_workout.id,
        exercise_id = pull_ups.id
    )
    db.session.add(work_exercise)

    work_exercise2 = Workout_Exercise(
        date = date.today(),
        workout_id = first_workout.id,
        exercise_id = push_ups.id
    )
    db.session.add(work_exercise2)


    db.session.commit()
    print('Tables are seeded')

