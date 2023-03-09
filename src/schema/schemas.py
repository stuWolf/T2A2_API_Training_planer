from main import ma

class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "username", "admin", "mobile_number", "email", "password")

    # pets = ma.List(ma.Nested("PetSchema", exclude=("user",)))

user_schema = UserSchema()
users_schema = UserSchema(many=True)

class WorkoutSchema(ma.Schema):
    class Meta:
        fields = ("id","rest_time", "rounds", "progres", "date")
        load_only = ["user_id"]

    user = ma.Nested("UserSchema")

    # pets = ma.List(ma.Nested("PetSchema", exclude=("user",)))

workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)


class WorkoutExerciseSchema(ma.Schema):
    class Meta:
        fields = ("id", "date")
        load_only = ["workout_id, exercise_id"]

    workout = ma.Nested("WorkoutSchema")
    exercise = ma.Nested("ExerciseSchema")
workout_exercise_schema = WorkoutExerciseSchema()
workout_exercises_schema = WorkoutExerciseSchema(many=True)

class ExerciseSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "description", "interval_time", "repetitions", "muscle_group", "level", "weight")
        
exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)
