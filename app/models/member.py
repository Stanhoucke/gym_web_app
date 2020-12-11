class Member():
    def __init__(self, first_name, last_name, gender, age, id = None):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.id = id

    def full_name(self, first_name, last_name):
        return f"{first_name} {last_name}"

    def increment_age(self, age):
        age += 1
        return f"{age}"