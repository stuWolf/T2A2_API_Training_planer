from main import ma

class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "username", "verified", "mobile_number", "post_code")

    # pets = ma.List(ma.Nested("PetSchema", exclude=("user",)))

user_schema = UserSchema()
users_schema = UserSchema(many=True)

class WorkoutSchema(ma.Schema):
    class Meta:
        fields = ("id", "progres", "date")
        load_only = ["user_id"]

    user = ma.Nested("UserSchema")

    # pets = ma.List(ma.Nested("PetSchema", exclude=("user",)))

workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)


class Workout_ExerciseSchema(ma.Schema):
    class Meta:
        fields = ("id", "date")
        load_only = ["workout_id, exercise_id"]

    workout = ma.Nested("WorkoutSchema")
    exercise = ma.Nested("ExerciseSchema")
workout_exercise_schema = Workout_ExerciseSchema()
workout_exercises_schema = Workout_ExerciseSchema(many=True)

class ExerciseSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "description", "interval_time", "repetitions", "rest_time", "rounds", "muscle_group", "level")
        

   

user_schema = ExerciseSchema()
users_schema = ExerciseSchema(many=True)
