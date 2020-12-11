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
    pass

def select_all():
    pass

def workouts(member):
    pass

# Update
def update(member):
    pass

# Delete
def delete(member):
    pass

def delete_all():
    pass