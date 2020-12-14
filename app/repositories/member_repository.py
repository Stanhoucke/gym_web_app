from db.run_sql import run_sql
from models.member import Member
from models.workout import Workout

# Create
def save(member):
    sql = "INSERT INTO members (first_name, last_name, gender, age) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [member.first_name, member.last_name, member.gender, member.age]
    result = run_sql(sql, values)
    member.id = result[0]['id']
    return member

# Read
def select(id):
    member = None

    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        member = Member(result['first_name'], result['last_name'], result['gender'], result['age'], result['id'])
    return member

def select_all():
    members = []

    sql = "SELECT * FROM members ORDER BY last_name ASC"
    results = run_sql(sql)

    for row in results:
        member = Member(row['first_name'], row['last_name'], row['gender'], row['age'], row['id'])
        members.append(member)
    return members


def workouts(member):
    workouts = []

    sql = "SELECT workouts.* FROM workouts INNER JOIN bookings ON bookings.workout_id = workouts.id WHERE bookings.member_id = %s"
    values = [member.id]
    results = run_sql(sql, values)

    for row in results:
        workout = Workout(row['name'], row['category'], row['upcoming'], row['date'], row['start_time'], row['id'])
        workouts.append(workout)
    return workouts

# Update
def update(member):
    sql = "UPDATE members SET (first_name, last_name, gender, age) = (%s, %s, %s, %s) WHERE id = %s"
    values = [member.first_name, member.last_name, member.gender, member.age, member.id]
    run_sql(sql, values)

# Delete
def delete(id):
    sql = "DELETE FROM members WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)