import models

class MemberStore:
	members = []
	last_id = 1

	def add(self, member):
		member.id = MemberStore.last_id
		MemberStore.members.append(member)
		MemberStore.last_id += 1

	def get_all(self):
		return MemberStore.members

	def get_by_id(self, id):
		all_members = self.get_all()
		result = None
		for member in all_members:
			if (member.id == id):
				result = member

		return result

	def get_by_name(self, name):
		all_members = self.get_all()
		result = None

		for member in all_members:
			if member.name == name:
				result = member

		return result

	def entity_exists(self, member):
		result = False

		if member in MemberStore.members:
			result = True

		return result

	def delete(self, id):
		member = self.get_by_id(id)
		if member:
			MemberStore.members.remove(member)

	def update(self, member):
		name = raw_input("Give the new name: \n")
		age = raw_input("Give the new age: \n")
		return models.Member(name, age)

class PostStore:
	posts = []

	def add(self, post):
		PostStore.posts.append(post)

	def get_all(self):
		for post in PostStore.posts:
			print(post)

	def get_by_id(self, id):
		all_posts = self.get_all()
		for post in all_posts:
			if post.id == id:
				return post
		return None

	def entity_exists(self, post):
		result = True
		if post not in PostStore.posts:
			result = False
		return result

	def delete(self, id):
		post = self.get_by_id(id)
		if post:
			PostStore.posts.remove(post)