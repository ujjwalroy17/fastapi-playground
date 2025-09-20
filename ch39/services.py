from db import engine
from sqlalchemy import text

# Using Raw Sql(INSERT)
def raw_sql_insert():
    with engine.connect() as conn:
        stmt = text("""
                    INSERT INTO users (name,email)
                    VALUES(:name,:email)
                    """)
        conn.execute(stmt, {"name" : "ujjwal","email" : "ujjwal@gmail.com"})
        conn.commit()
        
# Using Raw Sql(SELECT)
def raw_sql_select():
    with engine.connect() as conn:
        stmt = text("""
                    SELECT * FROM USERS WHERE email = :email
                    """)
        result = conn.execute(stmt, {"email":"ujjwal@gmail.com"}).first()
        return result  