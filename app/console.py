from models.member import Member
from models.workout import Workout
import repositories.member_repository as member_repository
import repositories.workout_repository as workout_repository

# member_repository.delete_all()

member_1 = Member("Dario", "Cologna", "male", 34)
member_repository.save(member_1)
workout_1 = Workout("Just Skate", "freestyle", True, "12/12/2020", "08:00")
workout_repository.save(workout_1)
workout_2 = Workout("Double Poling", "classic", False, "10/12/2020", "14:00")
workout_repository.save(workout_2)


member_1.age = 35
member_repository.update(member_1)

# print(member_repository.select(member_1.id))
# print(member_repository.select_all())

# member_repository.delete(member_1.id)