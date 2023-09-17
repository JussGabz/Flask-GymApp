from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from sqlalchemy.sql import func
import datetime

Base = declarative_base()
engine = create_engine("postgresql+psycopg2://postgres:admin@localhost/new_gymapp", echo=True)


# This session will be responsible for handling database connections
Session = sessionmaker(bind=engine)
session = Session()

# Test connection 

# with engine.connect() as conn:
#     result = conn.execute(text("select 'hello world'"))
#     print(result.all())

class PlanExercise(Base):
    __tablename__ = "plan_exercise"

    exercise_id = Column("exercise_id", ForeignKey("exercises.id"), primary_key=True)
    plan_id = Column("plan_id", ForeignKey("workout_plan.id"), primary_key=True)



class Exercise(Base):
    __tablename__ = "exercises"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String)
    target_area = Column("target_area", String)
    difficulty = Column("difficulty", String)
    time_created = Column("time_created", DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"ID: ({self.id}) Exercise: {self.name}"
    
    # Make as class Method - Helps to call without instantiating
    @classmethod
    def select_exercise(cls, session, exercise_name):

        exercise = session.query(Exercise).filter_by(name=exercise_name).first()
        if exercise:
            return exercise
        else:
            print("Exercise not found")
        
        session.close()
    
    def save_exercise(self, session):
        session.add(self)
        session.commit()
        session.close()

    def delete_exercise(self, session):
        session.delete(self)
        session.commit()
        session.close()
    
    def update_exercise(self, session, name=None, target_area=None, difficulty=None):
        if name:
            self.name = name
        if target_area:
            self.target_area = target_area
        if difficulty:
            self.difficulty = difficulty

        session.commit()
        session.close()


class WorkoutPlan(Base):
    __tablename__ = "workout_plan"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String)
    created_by = Column("created_by", String)
    date_created = Column("date_created", DateTime(timezone=True), server_default=func.now())

    exercises = relationship('Exercise', secondary="plan_exercise", backref="workout_plan")

    def __repr__(self):
        return f"Workout Plan ID: {self.id}, Name: {self.name}"
    
    def create_workout_plan(self):
        session.add(self)
        session.commit()

    @classmethod
    def select_workout_plan(cls, name):
        # Query Workout Plan by Name
        workout_plan = session.query(WorkoutPlan).filter_by(name=name).first()
        return workout_plan

    def update_workout_plan(self, session, name):
        if name:
            self.name = name
        
        session.commit()
        print("Workout Updated!")

    def delete_workout_plan(self, session):
        session.delete(self)
        session.commit()

    def add_exercises(self, session, exercises):
        with session:
            self.exercises = exercises
            session.commit()
        return "Exercise Added"

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

