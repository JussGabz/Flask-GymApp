from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
from models.engine import engine

plan_exercise = Table(
    "plan_exercise",
    Base.metadata,
    Column("exercise_id", ForeignKey("exercises.id")),
    Column("workoutplan_id", ForeignKey("workout_plan.id"))
)