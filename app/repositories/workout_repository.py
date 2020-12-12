from db.run_sql import run_sql
from models.workout import Workout
from models.member import Member

# Create
def save(workout):
    sql = "INSERT INTO workouts (name, category, upcoming, date, start_time) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [workout.name, workout.category, workout.upcoming, workout.date, workout.start_time]
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
        workout = Workout(result['name'], result['category'], result['upcoming'], result['date'], result['start_time'], result['id'])
    return workout

def select_all():
    workouts = []

    sql = "SELECT * FROM workouts"
    results = run_sql(sql)

    for row in results:
        workout = Workout(row['name'], row['category'], row['upcoming'], row['date'], row['start_time'], row['id'])
        workouts.append(workout)
    return workouts

def select_upcoming():
    workouts = []

    sql = "SELECT * FROM workouts"
    results = run_sql(sql)

    for row in results:
        workout = Workout(row['name'], row['category'], row['upcoming'], row['date'], row['start_time'], row['id'])
        if workout.upcoming:
            workouts.append(workout)
    return workouts


def members(workout):
    pass

# Update
def update(workout):
    sql = "UPDATE workouts SET (name, category, upcoming, date, start_time) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [workout.name, workout.category, workout.upcoming, workout.date, workout.start_time, workout.id]
    run_sql(sql, values)

# Delete
def delete(id):
    sql = "DELETE FROM workouts WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM workouts"
    run_sql(sql)