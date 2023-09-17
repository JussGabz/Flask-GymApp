from models import Exercise, WorkoutPlan, Base, engine, Session


class TestExercise:
    def setup_class(self):
        Base.metadata.create_all(engine)
        self.session = Session()
        self.exercise = Exercise(name="test_name", difficulty="test_difficulty")

    def teardown_class(self):
        self.session.rollback()
        self.session.close()

    def test_exercise_valid(self):

        # Add New Exercise 
        self.session.add(self.exercise)
        self.session.commit()
        
        # Query Exercise in Exercise Table 
        exercise = self.session.query(Exercise).filter_by(name="test_name").first()

        assert exercise.name != "wrong_test_name"
        # assert exercise.target_area == "test_target_area"
        assert exercise.difficulty == "test_difficulty"

class TestWorkOutPlan:
    def setup_class(self):
        Base.metadata.create_all(engine)
        self.session = Session()
        self.workout_plan = WorkoutPlan(name="test_workoutplan", created_by="test_user")

    def teardown_class(self):
        self.session.rollback()
        self.session.close()

    def test_workout_plan_valid(self):
        
        # Add Workout to DB
        self.session.add(self.workout_plan)
        self.session.commit()

        # Query Workout Plan in DB
        workout_plan = self.session.query(WorkoutPlan).filter_by(name="test_workoutplan").first()

        assert workout_plan.name == "test_workoutplan"
        assert workout_plan.created_by == "test_user"
        assert workout_plan.date_created != None




