from flask import Flask, Blueprint, render_template, request, redirect
from models.workout import Workout
import repositories.workout_repository as workout_repository

workouts_blueprint = Blueprint("workouts", __name__)

@workouts_blueprint.route("/workouts")
def workouts():
    workouts = workout_repository.select_all()
    return render_template("workouts/index.html", workouts=workouts)

@workouts_blueprint.route("/workouts/<id>")
def show_workout(id):
    workout = workout_repository.select(id)
    members = workout_repository.members(workout)
    return render_template("workouts/show.html", workout=workout, members=members)

