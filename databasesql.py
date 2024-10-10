import sqlite3
con=sqlite3.connect("batch7.db")
try:
    con.execute("create table std(roll_no int,name text,age int)")
except:
    pass

import sqlite3
con=sqlite3.connect("batch7.db")
try:
    con.execute("create table mark(roll_no int,sub text,mark int)")
except:
    pass


# con.execute("insert into std(roll_no,name,age)values(1,'abhi',15),(2,'anu',17),(3,'ezu',18)")
# con.commit()

con.execute("insert into mark(roll_no,sub,mark)values(1,'cs',75),(1,'che',70),(2,'cs',65),(4,'py',55)")
con.commit()


# roll=int(input("Enter roll num"))
# name=str(input("Enter name"))
# age=int(input("Enter age"))

# con.execute("insert into std(roll_no,name,age)values(?,?,?)",(roll,name,age))
# con.commit()

# lmt=int(input("enter limit"))
# for i in range(lmt):
#     roll=int(input("Enter roll num"))
#     name=str(input("Enter name"))
#     age=int(input("Enter age"))

#     con.execute("insert into std(roll_no,name,age)values(?,?,?)",(roll,name,age))   
#     con.commit()


# data=con.execute("select name,age from std")
# print(data)
# for i in data:
#     print(i) 

# data=con.execute("select * from std  where name='ezu'")
# for i in data:
#     print(i)

# a=str(input("enter name"))
# data=con.execute("select * from std  where name=?",(a,))
# for i in data:
#     print(i)


# con.execute("update std set name='aiu',age=15 where name='anu'")
# con.commit()

# a=str(input("enter new name"))
# b=str(input("enter old name"))
# con.execute("update std set name=? where name=? ",(a,b))
# con.commit()

# rollnum=int(input("enter roll num"))
# con.execute("delete from std where roll_no=?",(rollnum,))
# con.commit()

# data=con.execute("select * from std Where name like 'a%' ")
# for i in data:
#     print(i)

data=con.execute("select * from std order by name desc")
for i in data:
    print(i)