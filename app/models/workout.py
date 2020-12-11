class Workout():
    def __init__(self, name, category, upcoming, date, start_time, id = None):
        self.name = name
        self.category = category
        self.upcoming = upcoming
        self.date = date
        self.start_time = start_time
        self.id = id

    def date_time(self):
        return f"{self.date} {self.start_time}"