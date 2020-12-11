from models.member import Member
import repositories.member_repository as member_repository

member_1 = Member("Dario", "Cologna", "male", 34)
member_repository.save(member_1)