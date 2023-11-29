from flask import Flask, render_template, request, Response, abort
from models.exercise import Exercise
from models.workoutplans import WorkoutPlan
from models.engine import Session

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"


session = Session()


# Return List of exercises categories
# @app.route("/exercises-category")
# def get_exercise_categories():
#     return render_template("exercise_category.html", exercises=exercises)

# Return List of exercises
@app.route("/exercises", methods=["GET"])
def get_exercises():

    exercises = session.query(Exercise).all()

    # Return The Class of exercises
    return render_template("exercises.html", exercises=exercises)

@app.route("/exercises", methods=["POST"])
def create_exercise():
    request_data = request.get_json()

    exercise_name = request_data["name"]
    target_area = request_data["target_area"]
    exercise_difficulty = request_data["difficulty"]

    new_exercise = Exercise(
            name=exercise_name,
            target_area=target_area,
            difficulty=exercise_difficulty)
    
    new_exercise.save_exercise(session=session)

    exercises = session.query(Exercise).all()

    return render_template("exercises.html", exercises=exercises)


# Get Exercise by ID
@app.route("/exercise/<int:exercise_id>")
def get_exercise(exercise_id):

    exercise = session.query(Exercise).filter_by(id=exercise_id).first()

    if exercise is None:
        raise Exception("Exercise does not exist")

    # Return 
    return render_template("exercise.html", exercise=exercise)

# Delete Exercise by ID
@app.route("/exercise/<int:exercise_id>", methods=["DELETE"])
def delete_exercise(exercise_id):

    exercise = session.query(Exercise).filter_by(id=exercise_id).first()

    if exercise is not None:
        exercise.delete_exercise(session=session)

    return render_template("exercise.html", exercise=exercise)

# Update Exercise by ID
@app.route("/exercise/<int:exercise_id>", methods=["PUT"])
def update_exercise(exercise_id):

    exercise = session.query(Exercise).filter_by(id=exercise_id).first()

    if exercise is not None:
        exercise.update_exercise(session=session)
        return render_template("exercise.html", exercise=exercise)
    else:
        abort(404)

    




# Return List of Work out Plans 
@app.route("/workoutplans")
def workoutplans():
    return render_template("workoutplans.html")

@app.route("/workoutplan/<int:workoutplan_id>")
def show_workoutplan():
    return f"Workout Plan"
