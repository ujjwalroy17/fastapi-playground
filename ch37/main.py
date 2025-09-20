from tables import create_tables
from services import create_users,create_posts,Get_users_ordered_by_name,get_posts_latest_first,get_post_count_per_user

create_tables()

create_tables()
#Create Data
# create_users("sonam", "sonam@example.com")
# create_users("raj", "raj@example.com")
# create_posts(1, "Hello World", "This is Sonam's first post")
# create_posts(1, "Bye World", "This is Sonam's second post")
# create_posts(1, "No World", "This is Sonam's third post")
# create_posts(2, "Raj's Post 1", "Hi from Raj! 1")
# create_posts(2, "Raj's Post 2", "Hi from Raj! 2")

# ORDER BY ---->

# Get users ordered by name(A-Z)

# print(Get_users_ordered_by_name())


# Get all posts ordered by latest 

# print(get_posts_latest_first())


# GROUP BY ---->

print(get_post_count_per_user())
