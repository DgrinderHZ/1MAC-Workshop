""" Project testing!!! """
import models
import stores


def show_members(all_members):
	for member in all_members:
		print(member)

member1 = models.Member("Hassan", 22)
member2 = models.Member("Mohammad", 24)

post1 = models.Post("Classes", "OOP blueprints!")
post2 = models.Post("Inheritance", "It makes classes for reusability!")
post3 = models.Post("Variables", "Every code has Variables!")

member_store = stores.MemberStore()
post_store = stores.PostStore()

print("="*10 + " Members " + "="*10)
print member1
print member2
print("="*10 + " Posts " + "="*10)
print post1
print post2

member_store.add(member1)
member_store.add(member2)
print("="*10 + " Members Store " + "="*10)
all_members = member_store.get_all()

show_members(all_members)

post_store.add(post1)
post_store.add(post2)
post_store.add(post3)
print("="*10 + " Posts Store " + "="*10)
print(post_store.get_all())

print("="*10 + " Get member by ID " + "="*10)
print(member_store.get_by_id(1))

print("="*10 + " Get member by NAME " + "="*10)
print(member_store.get_by_name("Hassan"))

print("========= entity_exists test ========")
print(member_store.entity_exists(member1))
member3 = models.Member("Ali", 23)
print(member_store.entity_exists(member3))

print("========= delete test =========")
member_store.add(member3)
all_members = member_store.get_all()
show_members(all_members)
member_store.delete(2)
print("=========== after deletion: ")
all_members = member_store.get_all()
show_members(all_members)

print(":::END:::")


