from models.member import Member
from models.workout import Workout
from models.booking import Booking
import repositories.member_repository as member_repository
import repositories.workout_repository as workout_repository
import repositories.booking_repository as booking_repository
import datetime

member_repository.delete_all()
workout_repository.delete_all()
# booking_repository.delete_all()

member_1 = Member("Dario", "Cologna", "male", 34)
member_repository.save(member_1)
member_2 = Member("Guido", "Van Rossum", "male", 64)
member_repository.save(member_2)
workout_1 = Workout("Just Skate", "freestyle", True, datetime.date(2020, 12, 16), datetime.time(6, 15), 2)
workout_repository.save(workout_1)
workout_2 = Workout("Double Poling", "classic", False, datetime.date(2020, 12, 10), datetime.time(10,30), 3)
workout_repository.save(workout_2)
# booking_1 = Booking(member_1, workout_1)
# booking_repository.save(booking_1)
# booking_2 = Booking(member_1, workout_2)
# booking_repository.save(booking_2)
# booking_3 = Booking(member_2, workout_1)
# booking_repository.save(booking_3)

# # print(member_repository.select(member_1.id))
# # print(member_repository.select_all())
# # print(workout_repository.select(workout_1.id))
# # print(workout_repository.select_all())
# # print(workout_repository.select_upcoming())
# # print(booking_repository.select(booking_1.id))
# # print(booking_repository.select_all())

# # Join table selects
# print(member_repository.workouts(member_1))
# print(workout_repository.members(workout_1))

# member_1.age = 35
# member_repository.update(member_1)
# workout_2.date = "16/12/2020"
# workout_2.upcoming = True
# workout_repository.update(workout_2)

# # workout_repository.delete(workout_1.id)
# # member_repository.delete(member_1.id)
# # booking_repository.delete(booking_1.id)

# print(workout_1.start_time)
