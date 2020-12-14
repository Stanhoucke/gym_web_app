from db.run_sql import run_sql
from models.booking import Booking
import repositories.member_repository as member_repository
import repositories.workout_repository as workout_repository

# Create
def save(booking):
    sql = "INSERT INTO bookings (member_id, workout_id) VALUES (%s, %s) RETURNING id"
    values = [booking.member.id, booking.workout.id]
    result = run_sql(sql, values)
    booking.id = result[0]['id']
    return booking

# Read
def select(id):
    booking = None

    sql = "SELECT * FROM bookings WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        member = member_repository.select(result['member_id'])
        workout = workout_repository.select(result['workout_id'])
        booking = Booking(member, workout)
    return booking

def select_all():
    bookings = []

    sql = "SELECT * FROM bookings ORDER BY id DESC"
    results = run_sql(sql)

    for row in results:
        member = member_repository.select(row['member_id'])
        workout = workout_repository.select(row['workout_id'])
        booking = Booking(member, workout, row['id'])
        bookings.append(booking)
    return bookings

# Update

# Delete
def delete(id):
    sql = "DELETE FROM bookings WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)