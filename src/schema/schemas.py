from main import ma



class ExerciseSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "description", "interval_time", "repetitions", "muscle_group", "level", "weight")
        
exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)



class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "username", "admin", "mobile_number", "email", "password")

    # pets = ma.List(ma.Nested("PetSchema", exclude=("user",)))

user_schema = UserSchema()
users_schema = UserSchema(many=True)

class WorkoutSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ("id", "name", "rest_time", "rounds", "progres", "date", "user_id", "user")
        load_only = ["user_id"]
    # user = fields.Nested("UserSchema")
    user = ma.Nested("UserSchema", only=("email",))

    # user = ma.List(ma.Nested("UserSchema", only=("email",)))
    # user = ma.List(ma.Nested("UserSchem", exclude=("email",)))

workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)

class WorkoutExerciseSchema(ma.Schema):
    class Meta:
        fields = ("id", "date","workout_id", "exercise_id", "workout", "exercise")
        load_only = ["workout_id", "exercise_id"]

    workout = ma.Nested("WorkoutSchema")
    exercise = ma.Nested("ExerciseSchema")
workout_exercise_schema = WorkoutExerciseSchema()
workout_exercises_schema = WorkoutExerciseSchema(many=True)


