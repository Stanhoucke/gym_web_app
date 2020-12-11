import unittest
from models.booking import Booking
from models.member import Member
from models.workout import Workout

class TestBooking(unittest.TestCase):
    def setUp(self):
        self.member_1 = Member("Dario", "Cologna", "male", 34)
        self.workout_1 = Workout("Just Skate", "freestyle", True, "12/12/2020", "08:00")
        self.booking_1 = Booking(self.member_1, self.workout_1)

    def test_booking_has_member(self):
        self.assertEqual(self.member_1, self.booking_1.member)

    def test_booking_has_workout(self):
        self.assertEqual(self.workout_1, self.booking_1.workout)

