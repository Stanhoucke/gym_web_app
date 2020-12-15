import datetime

class Workout():
    def __init__(self, name, category, date, start_time, capacity, booked=0, id = None):
        self.name = name
        self.category = category
        self.date = date
        self.start_time = start_time
        self.capacity = capacity
        self.booked = booked
        self.id = id

    def date_time(self):
        return f"{self.date} {self.start_time}"

    def increment_booked(self):
        self.booked += 1

    def decrease_booked(self):
        self.booked -= 1

    def check_capacity(self):
        return self.booked < self.capacity

    def check_upcoming(self):
        return self.date >= datetime.date.today()