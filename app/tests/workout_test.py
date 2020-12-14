import unittest
from models.workout import Workout
import datetime

class TestWorkout(unittest.TestCase):
    def setUp(self):
        self.date = datetime.date(2020, 12, 16)
        self.workout_1 = Workout("Just Skate", "freestyle", True, self.date, "08:00")

    def test_workout_has_name(self):
        self.assertEqual("Just Skate", self.workout_1.name)

    def test_workout_has_category(self):
        self.assertEqual("freestyle", self.workout_1.category)

    def test_workout_has_upcoming(self):
        self.assertEqual(True, self.workout_1.upcoming)

    # Date and time tests
    def test_workout_has_date(self):
        self.assertEqual(self.date, self.workout_1.date)

    def test_workout_has_start_time(self):
        self.assertEqual("08:00", self.workout_1.start_time)

    # def test_date_time__returns_date_and_time(self):
        self.assertEqual("2020-12-16 08:00", self.workout_1.date_time())
    

    