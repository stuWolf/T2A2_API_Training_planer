from main import ma



class ExerciseSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ("id", "name", "description", "interval_time", "repetitions", "body_region", "level", "weight", "video")
        # load_only = ["id"]
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
        fields = ("id", "workout_name", "rest_time", "rounds","body_region", "level", "progres", "date", "user_id", "user")
        load_only = ["user_id"]
    # user = fields.Nested("UserSchema")
    user = ma.Nested("UserSchema", only=("email",))
workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)

class ProgresSchema(ma.Schema):
    
    class Meta:
        ordered = True
        fields = ("id", "progres_name", "weight", "mid_arm","waist","chest", "hip", "test_score", "date", "user_id", "user")
        load_only = ["user_id"]
    # user = fields.Nested("UserSchema")
    user = ma.Nested("UserSchema", only=("email",))

    # user = ma.List(ma.Nested("UserSchema", only=("email",)))
    # user = ma.List(ma.Nested("UserSchem", exclude=("email",)))

progres_schema = ProgresSchema()
progresses_schema = ProgresSchema(many=True)

class WorkoutExerciseSchema(ma.Schema):
    ordered = True
    class Meta:
        ordered = True
        fields = ("id", "date","workout_id", "exercise_id", "workout", "exercise")
        load_only = ["id", "workout_id", "exercise_id"]
    ordered = True
    workout = ma.Nested("WorkoutSchema", only=("workout_name", "rest_time", "rounds"))
    exercise = ma.Nested("ExerciseSchema", exclude = ("id",))
workout_exercise_schema = WorkoutExerciseSchema()
workout_exercises_schema = WorkoutExerciseSchema(many=True)


