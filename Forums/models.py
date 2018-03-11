
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
		return ("Title: {}\nBody: {}\n".format(self.title, self.body))


class MemberStore:
	members = []

	def add(self, member):
		self.members.append(member)

	def get_all(self):
		for member in self.members:
			print(member)


class PostStore:
	posts = []

	def add(self, post):
		self.posts.append(post)

	def get_all(self):
		for post in self.posts:
			print(post)
