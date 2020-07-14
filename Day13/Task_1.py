from sqlalchemy import create_engine

e = create_engine("sqlite:///task.db")
e.execute("""
   create table "group" (
       id integer primary key autoincrement,
       name varchar
   )
""")