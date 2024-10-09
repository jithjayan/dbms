import sqlite3
con=sqlite3.connect("batch7.db")
try:
    con.execute("create table std(roll_no int,name text,age int)")
except:
    pass


# con.execute("insert into std(roll_no,name,age)values(1,'abhi',15),(2,'anu',17),(3,'ezu',18)")
# con.commit()

# roll=int(input("Enter roll num"))
# name=str(input("Enter name"))
# age=int(input("Enter age"))

# con.execute("insert into std(roll_no,name,age)values(?,?,?)",(roll,name,age))
# con.commit()

lmt=int(input("enter limit"))
for i in range(lmt):
    roll=int(input("Enter roll num"))
    name=str(input("Enter name"))
    age=int(input("Enter age"))

    con.execute("insert into std(roll_no,name,age)values(?,?,?)",(roll,name,age))   
    con.commit()