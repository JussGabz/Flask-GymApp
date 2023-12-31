from sqlalchemy import Column, Integer, String, DateTime, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from models.engine import Session
from models.associations import plan_exercise # Import for exercises relationship
from . import Base

session = Session()

class WorkoutPlan(Base):
    __tablename__ = "workout_plan"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String)
    created_by = Column("created_by", String)
    date_created = Column("date_created", DateTime(timezone=True), server_default=func.now())
    # Use BackPopulates
    exercises = relationship("Exercise", secondary="plan_exercise", back_populates='workoutplans')

    def __repr__(self):
        return f"Workout Plan ID: {self.id}, Name: {self.name}"
    
    def create_workout_plan(self, session=session):
        with session:
            session.add(self)
            session.commit()

    @classmethod
    def select_workout_plan(cls, name, session=session):
        # Query Workout Plan by Name
        with session:
            workout_plan = session.query(WorkoutPlan).filter_by(name=name).first()
        return workout_plan

    def update_workout_plan(self, name, session=session):
        if name:
            self.name = name
        
        session.commit()
        print("Workout Updated!")

    def delete_workout_plan(self, session):
        session.delete(self)
        session.commit()
    
    def get_exercises(self, session=session):
        workout_plan = WorkoutPlan.select_workout_plan(name=self.name, session=session)

        if workout_plan.exercises is None:
            return []

        return workout_plan.exercises


    def add_exercises(self, exercises, session=session):
        # TODO - CHeck if exercises exist first before adding exercise

        
        with session:
            session.add(self)
            for exercise in exercises:
                session.add(exercise)
            self.exercises = exercises

            session.commit()
        return "Exercise Added"


