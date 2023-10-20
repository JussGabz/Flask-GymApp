from sqlalchemy import Column, Integer, String, DateTime, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from models.engine import Session
from . import Base

session = Session()

plan_exercise = Table(
    "plan_exercise",
    Base.metadata,
    Column("exercise_id", ForeignKey("exercises.id")),
    Column("plan_id", ForeignKey("workout_plan.id"))
)

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


