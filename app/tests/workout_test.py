import unittest
from models.workout import Workout

class TestWorkout(unittest.TestCase):
    def setUp(self):
        self.workout_1 = Workout("Just Skate", "freestyle", True, "12/12/2020", "08:00")

    def test_workout_has_name(self):
        self.assertEqual("Just Skate", self.workout_1.name)

    def test_workout_has_category(self):
        self.assertEqual("freestyle", self.workout_1.category)

    def test_workout_has_upcoming(self):
        self.assertEqual(True, self.workout_1.upcoming)

    # Date and time tests
    def test_workout_has_date(self):
        self.assertEqual("12/12/2020", self.workout_1.date)

    def test_workout_has_start_time(self):
        self.assertEqual("08:00", self.workout_1.start_time)

    def test_date_time__returns_date_and_time(self):
        self.assertEqual("12/12/2020 08:00", self.workout_1.date_time())
    

    