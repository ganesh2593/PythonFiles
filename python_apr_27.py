

##def Trange(n):
##    if n in range(3,8):
##        print(" %s is within the range"%str(n))
##    else:
##        print("the number is not in range")
##Trange(5)

import sqlite3
def myDb(query,DB):
    cot=sqlite3.connect('ganesh1.db')
    exe_query=cot.execute(query)
    query_output=exe_query.fetchall()
    print(query_output)
    cot.commit()
    cot.close()

#query="""create table student1('name' text,'age' integer)"""
#query="""insert into student1(name,age)values('ganesh',55)"""
query="""select * from student1"""
myDb(query,"ganesh1.db")
    
