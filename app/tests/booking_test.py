import unittest
from models.booking import Booking
from models.member import Member
from models.workout import Workout
import datetime

class TestBooking(unittest.TestCase):
    def setUp(self):
        self.member_1 = Member("Dario", "Cologna", "male", 34)

        self.date = datetime.date(2020, 12, 16)
        self.time = datetime.time(6, 15)
        self.workout_1 = Workout("Just Skate", "freestyle", True, self.date, self.time, 3)
        self.booking_1 = Booking(self.member_1, self.workout_1)

    def test_booking_has_member(self):
        self.assertEqual(self.member_1, self.booking_1.member)

    def test_booking_has_workout(self):
        self.assertEqual(self.workout_1, self.booking_1.workout)

    # Methods
    def test_booking_checks_capacity_and_updates_workout_booked(self):
        self.assertEqual(True, self.booking_1.check_capacity())
        self.assertEqual(1, self.booking_1.workout.booked)

