from flask import Flask, render_template

from controllers.members_controller import members_blueprint
from controllers.workouts_controller import workouts_blueprint
from controllers.bookings_controller import bookings_blueprint

import repositories.workout_repository as workout_repository

app = Flask(__name__)

app.register_blueprint(members_blueprint)
app.register_blueprint(workouts_blueprint)
app.register_blueprint(bookings_blueprint)

@app.route('/')
def home():
    workouts = workout_repository.select_upcoming()
    return render_template('index.html', workouts=workouts)

if __name__ == '__main__':
    app.run(debug=True)