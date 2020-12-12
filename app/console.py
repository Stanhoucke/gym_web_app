from models.member import Member
import repositories.member_repository as member_repository

# member_repository.delete_all()

member_1 = Member("Dario", "Cologna", "male", 34)
member_repository.save(member_1)

member_1.age = 35
member_repository.update(member_1)

# print(member_repository.select(member_1.id))
# print(member_repository.select_all())

# member_repository.delete(member_1.id)