from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from models.engine import Session
from models.associations import plan_exercise
from . import Base

# This session will be responsible for handling database connections
session = Session()

class Exercise(Base):
    __tablename__ = "exercises"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String)
    target_area = Column("target_area", String)
    difficulty = Column("difficulty", String)
    time_created = Column("time_created", DateTime(timezone=True), server_default=func.now())

    exercises = relationship("WorkoutPlan", secondary="plan_exercise")

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