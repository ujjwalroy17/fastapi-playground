from tables import create_tables, drop_tables
import asyncio
from services import create_user,get_user_by_id,get_all_user,update_user_email,delete_User
async def main():
    # Create Tables
    # await create_tables()
    
    # Create Data
    # await create_user('sonam',"sonam@example.com")
    # await create_user('raj','raj@eample.com')
    
    # Read Data
    # print(await get_user_by_id(1))
    # print(await get_all_user())
    
    
    # Update Data
    # await update_user_email(1,'sonam@newdomain.com')
    
    # Delete Data
    await delete_User(2)
    
asyncio.run(main())