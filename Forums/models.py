
class Member:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		self.id = 0

	def __str__(self):
		return ("Name: {}\t\tAge: {}".format(self.name, self.age))


class Post:
	def __init__(self, title, body):
		self.title = title
		self.body = body
		self.id = 0

	def __str__(self):
		return ("Title: {}\nBody: {}\n".format(self.title, self.body))


