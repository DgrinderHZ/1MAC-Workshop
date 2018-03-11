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
