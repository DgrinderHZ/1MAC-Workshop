import models


member1 = models.Member("Hassan", 22)
member2 = models.Member("Mohammad", 24)

post1 = models.Post("Classes", "OOP blueprints!")
post2 = models.Post("Inheritance", "It makes classes for reusability!")
post3 = models.Post("Variables", "Every code has Variables!")

member_store = models.MemberStore()
post_store = models.PostStore()

print("="*10 + " Members " + "="*10)
print member1
print member2
print("="*10 + " Posts " + "="*10)
print post1
print post2

member_store.add(member1)
member_store.add(member2)
print("="*10 + " Members Store " + "="*10)
print(member_store.get_all())

post_store.add(post1)
post_store.add(post2)
post_store.add(post3)
print("="*10 + " Posts Store " + "="*10)
print(post_store.get_all())

print(":::END:::")


