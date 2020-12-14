from flask import Flask, Blueprint, render_template, request, redirect
from models.workout import Workout
import repositories.workout_repository as workout_repository
import datetime

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

# New
@workouts_blueprint.route("/workouts/new")
def new_workout():
    return render_template("workouts/new.html")

@workouts_blueprint.route('/workouts', methods=['POST'])
def create_workout():
    # Form data
    name        = request.form['name']
    category    = request.form['category']
    upcoming    = request.form['upcoming']
    # Format date
    date        = request.form['date']
    # Split the date into a list
    split_date = date.split('-')
    # create a new date object
    date = datetime.date(int(split_date[0]), int(split_date[1]), int(split_date[2]))

    start_time  = request.form['start_time']
    # Create new Workout object
    workout = Workout(name, category, upcoming, date, start_time)
    # Save to db
    workout_repository.save(workout)
    # Redirect
    return redirect('/workouts')

# Edit
@workouts_blueprint.route('/workouts/<id>/edit', methods=['GET'])
def edit_workout(id):
    workout = workout_repository.select(id)
    return render_template('workouts/edit.html', workout=workout)

@workouts_blueprint.route('/workouts/<id>', methods=['POST'])
def update_workout(id):
    # Form data
    name        = request.form['name']
    category    = request.form['category']
    upcoming    = request.form['upcoming']
    date        = request.form['date']
    start_time  = request.form['start_time']
    # Create new Workout object
    workout = Workout(name, category, upcoming, date, start_time, id)
    # Update in db
    workout_repository.update(workout)
    # Redirect
    return redirect('/workouts')

