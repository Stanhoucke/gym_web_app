class Workout():
    def __init__(self, name, category, upcoming, date, time, id = None):
        self.name = name
        self.category = category
        self.upcoming = upcoming
        self.date = date
        self.time = time
        self.id = id

    def date_time(self, date, time):
        return f"{date} {time}"