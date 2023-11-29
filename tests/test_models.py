# from models import Exercise, WorkoutPlan, Base, engine, Session
from models import Base
from models.exercise import Exercise
from models.workoutplans import WorkoutPlan
from models.engine import engine, Session


class TestExercise:
    def setup_class(self):
        Base.metadata.create_all(engine)
        self.session = Session()
        self.exercise = Exercise(name="test_name", difficulty="test_difficulty")



    def teardown_class(self):
        self.session.rollback()
        self.session.close()


    def test_save_exercise(self):

        self.exercise.save_exercise(session=self.session)

        exercise = self.session.query(Exercise).filter_by(name="test_name").first()

        assert exercise.name == "test_name"
        assert exercise.difficulty == "test_difficulty"
    
    def test_select_exercise(self):

        exercise = self.exercise.select_exercise(session=self.session, exercise_name="test_name")

        assert exercise.name == "test_name"

    def test_delete_exercise(self):
        
        # Save Exercise Object 
        self.exercise.save_exercise(session=self.session)

        # Query Exercise
        exercise = self.session.query(Exercise).filter_by(name="test_name")
        assert exercise is not None
    
        # Delete Exercise Object 
        self.exercise.delete_exercise(session=self.session)
        
        # Query Deleted Exercise -> Should return None
        deleted_test_name_2 = self.session.query(Exercise).filter_by(name="test_name").first()
        
        assert deleted_test_name_2 is None
        


class TestWorkOutPlan:
    def setup_class(self):
        Base.metadata.create_all(engine)
        self.session = Session()
        self.workout_plan = WorkoutPlan(name="test_workoutplan", created_by="test_user", exercises=[])


    def teardown_class(self):
        self.session.rollback()
        self.session.close()

    def test_create_workout_plan(self):

        # Add Workout to DB
        self.workout_plan.create_workout_plan()
        
        # Query Workout Plan in DB
        workout_plan = self.session.query(WorkoutPlan).filter_by(name="test_workoutplan").first()

        assert workout_plan.name == "test_workoutplan"
        assert workout_plan.created_by == "test_user"
        assert workout_plan.date_created != None
    
    def test_add_exercises(self):

        # Create Workout Plan
        self.workout_plan.create_workout_plan(session=self.session)
        
        # Create Exercise Object 
        first_exercise = Exercise(name="test_exercise", difficulty="test_difficulty")
       
        # Save Exercise Objects 
        first_exercise.save_exercise(session=self.session)
        
        # Query Objects
        first_existing_exercise = Exercise.select_exercise(session=self.session, exercise_name="test_exercise")

        # Query Workout Plan
        workout_plan = WorkoutPlan.select_workout_plan(name="test_workoutplan", session=self.session)

        # Ensure the workout_plan instance is associated with the session
        self.session.add(workout_plan)

        # Add Existing Exercises
        workout_plan.add_exercises(session=self.session, exercises=[first_existing_exercise])

        # Commit the changes
        self.session.commit()

        assert workout_plan.exercises == [first_existing_exercise]

    def test_add_exercises(self):
        # Create Workout Plan
        self.workout_plan.create_workout_plan(session=self.session)
        
        # Create Exercise Object 
        first_exercise = Exercise(name="test_exercise", difficulty="test_difficulty")

        # Save Exercise Object
        first_exercise.save_exercise(session=self.session)

        # Query Objects
        first_existing_exercise = self.session.query(Exercise).filter_by(name="test_exercise").first()

        # Query Workout Plan
        workout_plan = WorkoutPlan.select_workout_plan(name="test_workoutplan", session=self.session)

        # Add Existing Exercises
        workout_plan.add_exercises(session=self.session, exercises=[first_existing_exercise])

        # Query Workout
        workout_exercises = self.session.query(WorkoutPlan).filter_by(name="test_workoutplan").first()

        # Add exercise to session
        self.session.add(first_existing_exercise)
        
        assert workout_exercises.exercises == [first_existing_exercise]

    





