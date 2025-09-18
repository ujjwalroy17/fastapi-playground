from tables import create_tables
from services import create_users,create_posts,get_user_by_id,get_all_users,get_posts_by_user,update_user_email,delete_post

# create tables
create_tables()

#create users --->

# create_users('Ujjwal', 'ujjwal@gmail.com')
# create_users('Raj','raj@gmail.com')

# create_posts(1 , "hello World" , "This is Ujjwal's first post")
# create_posts(2,"Raj's Post","Hi from Raj!")

# Get data --->

# print(get_user_by_id(1))

# print(get_all_users())

# print(get_posts_by_user(2))

# Update data --->

# update_user_email(1,'ujjwal@newdomain.in')

# delete post --->

delete_post(2)

