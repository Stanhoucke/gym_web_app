import unittest
from models.workout import Workout
import datetime

class TestWorkout(unittest.TestCase):
    def setUp(self):
        self.date = datetime.date(2020, 12, 16)
        self.time = datetime.time(6, 15)
        self.workout_1 = Workout("Just Skate", "freestyle", True, self.date, self.time, 3)

    def test_workout_has_name(self):
        self.assertEqual("Just Skate", self.workout_1.name)

    def test_workout_has_category(self):
        self.assertEqual("freestyle", self.workout_1.category)

    def test_workout_has_upcoming(self):
        self.assertEqual(True, self.workout_1.upcoming)
    
    def test_workout_has_no_members_booked(self):
        self.assertEqual(0, self.workout_1.booked)

    def test_workout_has_capacity(self):
        self.assertEqual(3, self.workout_1.capacity)

    # Date and time tests
    def test_workout_has_date(self):
        self.assertEqual(self.date, self.workout_1.date)

    def test_workout_has_start_time(self):
        self.assertEqual(self.time, self.workout_1.start_time)

    def test_date_time__returns_date_and_time(self):
        self.assertEqual("2020-12-16 06:15:00", self.workout_1.date_time())

    # Capacity tests
    def test_increment_booked__returns_1(self):
        self.workout_1.increment_booked()
        self.assertEqual(1, self.workout_1.booked)
    

    