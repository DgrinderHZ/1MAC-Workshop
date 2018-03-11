class MemberStore:
	members = []

	def add(self, member):
		self.members.append(member)

	def get_all(self):
		#for member in self.members:
		#	print(member)
		return self.members

	def get_by_id(self, id):
		all_members = self.get_all()
		result = -1
		i = 0
		for member in all_members:
			if (i == id):
				result = member
			i += 1

		return result

	def get_by_name(self, name):
		all_members = self.get_all()
		result = -1

		for member in all_members:
			if member.name == name:
				result = member

		return result


class PostStore:
	posts = []

	def add(self, post):
		self.posts.append(post)

	def get_all(self):
		for post in self.posts:
			print(post)