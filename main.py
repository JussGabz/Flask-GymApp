from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/exercises")
def exercises():
    return "Exercises"

@app.route("/workoutplans")
def workoutplans():
    return "Workout Plans"