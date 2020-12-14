class Workout():
    def __init__(self, name, category, upcoming, date, start_time, capacity, id = None):
        self.name = name
        self.category = category
        self.upcoming = upcoming
        self.date = date
        self.start_time = start_time
        self.booked = 0
        self.capacity = capacity
        self.id = id

    def date_time(self):
        return f"{self.date} {self.start_time}"

    def increment_booked(self):
        self.booked += 1