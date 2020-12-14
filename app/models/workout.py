class Workout():
    def __init__(self, name, category, upcoming, date, start_time, capacity, booked=0, id = None):
        self.name = name
        self.category = category
        self.upcoming = upcoming
        self.date = date
        self.start_time = start_time
        self.capacity = capacity
        self.booked = booked
        self.id = id

    def date_time(self):
        return f"{self.date} {self.start_time}"

    def increment_booked(self):
        self.booked += 1

    def check_capacity(self):
        return self.booked < self.capacity