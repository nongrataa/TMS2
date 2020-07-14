from sqlalchemy import create_engine
#Подключение к БД
e = create_engine("sqlite:///test.db")

#Создание таблицы
e.execute("""
create table user (
id integer primary key autoincrement, firstname varchar,
lastname varchar
) """)


#Добавление данных в таблицу
# e.execute("""
# insert into user (firstname, lastname)
# values('Alex','Varkalov')
# """)

# e.execute("""
# create table maintable (
# id integer primary key autoincrement, firstname varchar,
# lastname varchar, phone integer
# ) """)

# e.execute("""
# insert into maintable(firstname,lastname,phone)
# values('Aliaksandr','Hushcha','375298826464')
# """)
#
# result = e.execute("""SELECT * FROM maintable""")
# for maintable in result:
#     print(maintable)