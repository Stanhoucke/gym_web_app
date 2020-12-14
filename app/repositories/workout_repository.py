from db.run_sql import run_sql
from models.workout import Workout
from models.member import Member

# Create
def save(workout):
    sql = "INSERT INTO workouts (name, category, upcoming, date, start_time, capacity, booked) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [workout.name, workout.category, workout.upcoming, workout.date, workout.start_time, workout.capacity, workout.booked]
    result = run_sql(sql, values)
    workout.id = result[0]['id']
    return workout

# Read
def select(id):
    workout = None

    sql = "SELECT * FROM workouts WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        workout = Workout(result['name'], result['category'], result['upcoming'], result['date'], result['start_time'], result['capacity'], result['booked'], result['id'])
    return workout

def select_all():
    workouts = []

    sql = "SELECT * FROM workouts ORDER BY date DESC"
    results = run_sql(sql)

    for row in results:
        workout = Workout(row['name'], row['category'], row['upcoming'], row['date'], row['start_time'], row['capacity'], row['booked'], row['id'])
        workouts.append(workout)
    return workouts

def select_upcoming():
    workouts = []

    sql = "SELECT * FROM workouts ORDER BY date ASC"
    results = run_sql(sql)

    for row in results:
        workout = Workout(row['name'], row['category'], row['upcoming'], row['date'], row['start_time'], row['capacity'], row['booked'], row['id'])
        if workout.upcoming:
            workouts.append(workout)
    return workouts

def members(workout):
    members = []

    sql = "SELECT members.* FROM members INNER JOIN bookings ON bookings.member_id = members.id WHERE bookings.workout_id = %s"
    values = [workout.id]
    results = run_sql(sql, values)

    for row in results:
        member = Member(row['first_name'], row['last_name'], row['gender'], row['age'], row['id'])
        members.append(member)
    return members

# Update
def update(workout):
    sql = "UPDATE workouts SET (name, category, upcoming, date, start_time, capacity, booked) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [workout.name, workout.category, workout.upcoming, workout.date, workout.start_time, workout.capacity, workout.booked, workout.id]
    run_sql(sql, values)

# Delete
def delete(id):
    sql = "DELETE FROM workouts WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM workouts"
    run_sql(sql)