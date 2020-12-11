import unittest
from models.member import Member

class TestMember(unittest.TestCase):

    def setUp(self):
        self.member_1 = Member("Dario", "Cologna", "male", 34)

    # Name tests
    def test_member_has_first_name(self):
        self.assertEqual("Dario", self.member_1.first_name)

    def test_member_has_last_name(self):
        self.assertEqual("Cologna", self.member_1.last_name)
    
    def test_full_name__returns_first_and_last_name(self):
        self.assertEqual("Dario Cologna", self.member_1.full_name())

    # Gender attribute test
    def test_member_has_gender(self):
        self.assertEqual("male", self.member_1.gender)
       