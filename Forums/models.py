
class Member:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __str__(self):
		return ("Name: {}\t\tAge: {}".format(self.name, self.age))


class Post:
	def __init__(self, title, body):
		self.title = title
		self.body = body

	def __str__(self):
		return ("Title: {}\nBody: {}".format(self.title, self.body))
