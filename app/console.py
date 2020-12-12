from models.member import Member
from models.workout import Workout
from models.booking import Booking
import repositories.member_repository as member_repository
import repositories.workout_repository as workout_repository
import repositories.booking_repository as booking_repository

# member_repository.delete_all()
# workout_repository.delete_all()
# booking_repository.delete_all()

member_1 = Member("Dario", "Cologna", "male", 34)
member_repository.save(member_1)
workout_1 = Workout("Just Skate", "freestyle", True, "12/12/2020", "08:00")
workout_repository.save(workout_1)
workout_2 = Workout("Double Poling", "classic", False, "10/12/2020", "14:00")
workout_repository.save(workout_2)
booking_1 = Booking(member_1, workout_1)
booking_repository.save(booking_1)
booking_2 = Booking(member_1, workout_2)
booking_repository.save(booking_2)

# print(member_repository.select(member_1.id))
# print(member_repository.select_all())
# print(workout_repository.select(workout_1.id))
# print(workout_repository.select_all())
# print(workout_repository.select_upcoming())
print(booking_repository.select(booking_1.id))
print(booking_repository.select_all())

member_1.age = 35
member_repository.update(member_1)
workout_2.date = "16/12/2020"
workout_2.upcoming = True
workout_repository.update(workout_2)

# workout_repository.delete(workout_1.id)
# member_repository.delete(member_1.id)