class Booking():
    def __init__(self, member, workout, id = None):
        self.member = member
        self.workout = workout
        self.id = id

    # Check workout capacity
    def check_capacity(self):
        if self.workout.booked < self.workout.capacity:
            # If capacity, update numbers booked in workout
            self.workout.increment_booked()
            return True
        else:
            return False