import models
import stores


def show_members():
	print("=" * 30)

	all_members = member_store.get_all()
	for member in all_members:
		print(member)

	print("=" * 30)

def create_members(total_members):
	members_list = []
	for i in range(0, total_members):
		name = raw_input("Give member's name: \n")
		age = raw_input("Give member's age: \n")
		members_list.append(models.Member(name,age))
		print(members_list[-1])
	print("=" * 30)
	return members_list

def create_posts(totals_posts):
	posts_list = []
	for i in range(0, totals_posts):
		title = raw_input("Give post's title: \n")
		body = raw_input("Give post's body: \n")
		posts_list.append(models.Post(title, body))
		print(posts_list[-1])
	print("=" * 30)
	return posts_list

def store_members(members_list, member_store):
	for member in members_list:
		member_store.add(member)

def store_posts(posts_list, post_store):
	for post in posts_list:
		post_store.add(post)

def delete_with_catch_exeptions(num):
	try:
		member_store.delete(num)
	except ValueError:
		print("delete catched an exeption! reconsider your demand!")

def modify_object(member_store, name):
	""" Takes a members name, and updates his info """

	new_name = raw_input("New name: \n")
	new_age = raw_input("New age: \n")
	new_member = models.Member(new_name, new_age)
	member_to_update = member_store.get_by_name(name)

	if member_to_update == None:
		print("Sorry! This member name does not exit!")
	else:
		new_id = member_to_update.id
		new_member.id = new_id
		member_store.update(new_member)

def get_by_id_should_retrieve_same_object(member_store, member2):
    member2_retrieved = member_store.get_by_id(member2.id)

    if member2 is member2_retrieved:
        print("member2 and member2_retrieved are matching !")

def store_should_get_members_by_name(member_store):

    print("*" * 30)
    print("Getting by name:")
    members_by_name_retrieved = member_store.get_by_name("Mohammed")
    print_members_list(members_by_name_retrieved)

def show_members_with_posts(member_store, post_store):
	members_with_posts = member_store.get_members_with_posts(post_store.get_all())

	for member_with_posts in members_with_posts:
		print("{} has posts:".format(member_with_posts))
		for post in member_with_posts.posts:
			print("\t\t{}".format(post))

		print("=" * 10)

def show_top_two(member_store, post_store):
    top_two_members = member_store.get_top_two(post_store.get_all())

    for member_with_posts in top_two_members:
        print("{} has the following posts:".format(member_with_posts))
        for post in member_with_posts:
            print("\t\t{}".format(post))



member_store = stores.MemberStore()
post_store = stores.PostStore()

print("="*10 + " Members " + "="*10)
members_list = create_members(2)
print("="*10 + " Posts " + "="*10)
posts_list = create_posts(2)

store_members(members_list, member_store)
store_posts(posts_list, post_store)

print("="*10 + " Members Store " + "="*10)
show_members()

print("="*10 + " Posts Store " + "="*10)
print(post_store.get_all())

print("="*10 + " Get member by ID " + "="*10)
get_by_id_should_retrieve_same_object(member_store, members_list[0])

print("="*10 + " Get member by NAME " + "="*10)
print(member_store.get_by_name("Hassan"))

print("========= entity_exists test ========")
print(member_store.entity_exists(members_list[0]))

print("========= delete test =========")
delete_with_catch_exeptions(1)

print("=========== after deletion: ")
show_members()

print("=========== Update ======")
modify_object(member_store, "Hassan")

print("=========== after Update: ")
show_members()
print("========== members with posts")
show_members_with_posts(member_store, post_store)

print(":::END:::")


