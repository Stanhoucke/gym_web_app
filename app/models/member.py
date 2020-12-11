class Member():
    def __init__(self, first_name, last_name, gender, age, id = None):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.id = id

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def increment_age(self):
        self.age += 1
        return self.age