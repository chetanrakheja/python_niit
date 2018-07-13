import sqlite3
conn=sqlite3.connect("Chetan.db")


'''
createTable="create table student(id int primary key,name text not null, address text)"
conn.execute(createTable)
'''

'''
EnteredId=input("Enter Id ")
EnteredName=input("enter name ")
EnteredAddr=input("enter address ")
conn.execute("insert into student (id,name,address) values(?,?,?)",(EnteredId,EnteredName,EnteredAddr))
conn.commit()
'''

deleteDate="delete from student where id = 11"
curr=conn.execute(deleteDate)

selectAll="select * from student"
curr=conn.execute(selectAll)
print()
print()
print()
for c in curr:
	print(c[0],"\t",c[1],"\t",c[2])



