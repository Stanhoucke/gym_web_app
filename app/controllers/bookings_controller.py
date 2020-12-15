from flask import Flask, Blueprint, render_template, request, redirect
from models.booking import Booking
from models.workout import Workout
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.workout_repository as workout_repository

bookings_blueprint = Blueprint("bookings", __name__)

@bookings_blueprint.route("/bookings")
def bookings():
    bookings = booking_repository.select_all()
    return render_template("bookings/index.html", bookings=bookings)

# New booking
@bookings_blueprint.route("/bookings/new")
def new_booking():
    members = member_repository.select_all()
    workouts = workout_repository.select_all()
    return render_template("bookings/new.html", members=members, workouts=workouts)


@bookings_blueprint.route("/bookings", methods=["POST"])
def create_booking():
    # Get data from form
    member_id   = request.form['member']
    workout_id  = request.form['workout']
    # Select existing member and workout
    member = member_repository.select(member_id)
    workout = workout_repository.select(workout_id)
    # Create new booking object
    booking = Booking(member, workout)
    # Save to db
    booking_repository.save(booking)
    # Increment booking to workout and update workout
    booking.workout.increment_booked()
    workout_repository.update(workout)
    # Redirect
    return redirect('/bookings')

# Delete booking
@bookings_blueprint.route("/bookings/<id>/delete", methods=['POST'])
def remove_booking(id):
    # Select workout from booking
    booking = booking_repository.select(id)
    workout_id = booking.workout.id
    workout = workout_repository.select(workout_id)
    # Delete booking
    booking_repository.delete(id)
    # Decrease booked in workout and updte db
    workout.decrease_booked()
    workout_repository.update(workout)
    return redirect('/bookings')

