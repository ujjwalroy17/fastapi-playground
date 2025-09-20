from tables import create_tables
from services import create_users,create_posts,get_posts_with_author

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

print(get_posts_with_author())
