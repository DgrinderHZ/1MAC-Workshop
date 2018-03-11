import models


member1 = models.Member("Hassan", 22)
member2 = models.Member("Mohammad", 24)

post1 = models.Post("Classes", "OOP blueprints!")
post2 = models.Post("Inheritance", "It makes classes for reusability!")
post3 = models.Post("Variables", "Every code has Variables!")

print("="*10 + " Members " + "="*10)
print member1
print member2
print("="*10 + " Posts " + "="*10)
print post1
print post2