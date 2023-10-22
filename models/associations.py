from sqlalchemy import Table, Column, ForeignKey

from . import Base

plan_exercise = Table(
    "plan_exercise",
    Base.metadata,
    Column("exercise_id", ForeignKey("exercises.id")),
    Column("plan_id", ForeignKey("workout_plan.id"))
)