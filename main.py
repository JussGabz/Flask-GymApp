from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"

# List of exewrcises
exercises = [
    {
        "name": "Chest Press",
        "target_area": "Chest",
        "difficulty": "Hard"
    },
    {
        "name": "Back Rows",
        "target_area": "Back",
        "difficulty": "Hard"
    },
    {
        "name": "Leg Press",
        "target_area": "Leg",
        "difficulty": "Hard"
    }
]



# Return List of exercises categories
@app.route("/exercises-category")
def get_exercise_categories():
    return render_template("exercise_category.html", exercises=exercises)

# Return List of exercises
@app.route("/exercises")
def get_exercises():
    return render_template("exercises.html", exercises=exercises)

# Show Exercise by ID
@app.route("/exercise/<int:exercise_id>")
def show_exercise(exercise_id):
    return f"Exercise ID: {exercise_id}"

# Return List of Work out Plans 
@app.route("/workoutplans")
def workoutplans():
    return render_template("workoutplans.html")

@app.route("/workoutplan/<int:workoutplan_id>")
def show_workoutplan():
    return f"Workout Plan"