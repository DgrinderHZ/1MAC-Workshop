import models
import itertools
import copy

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
                break

        return result

    def get_by_name(self, name):
        all_members = self.get_all()

        for member in all_members:
            if member.name == name:
                yield member

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
        all_members = self.get_all()
        for index, current_member in enumerate(all_members):
            if member.id == current_member.id:
                MemberStore.members[index] = member
                break

    def get_members_with_posts(self, all_posts):
        all_members = copy.deepcopy(self.get_all())

        for member, post in itertools.product(all_members, all_posts):
            if member.id == post.member_id:
                member.posts.append(post)

        for member in all_members:
            yield member
    def get_top_two(self, all_posts):
        all_members = self.get_members_with_posts(all_posts)

        # sorting to get the top two
        all_posts = sorted(all_members, key=lambda x: len(x.posts), reverse=True)

        return all_members[0:2]


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

    def update(self, post):
        all_posts = self.get_all()
        for index, current_post in enumerate(all_members):
            if post.id == current_post.id:
                PostStore.posts[index] = post
                break