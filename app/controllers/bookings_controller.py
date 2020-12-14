from flask import Flask, Blueprint, render_template, request, redirect
from models.booking import Booking
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

