from models import create_tables
from services import *

# create_tables()

# Create Data
# result = create_user("sonam","sonam@example.com")
# print(result)
# create_user("raj","raj@example.com")
# create_post(1,"Hello world","This is Sonam's first post")
# create_post(2,"Raj's Post","hi from Raj!")
# create_post(2,"Raj's Post New","hi from Raj! New")


# Get Data

# result = get_user_by_id(1)
# print(result)

# print(get_post_by_id(1))

# get all data

# print(get_all_users())

# print(get_posts_by_user(2))


# Update data

# print(update_user_email(1,"sonam@newdomain.com"))

# delete data

# delete_post(3)

# Order by

print(get_users_ordered_by_name())
