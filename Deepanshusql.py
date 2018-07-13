import sqlite3
conn=sqlite3.connect("deepanshu.db")
#create="CREATE TABLE student(id int primary key,name text, address text)"
#conn.execute(create)
print("Choose From The Following Options")
print("Enter The Option Number\n1. Insert\n2. Retrieve")
menu=int(input(" Enter Your Choice Here "))
if menu==1:
	number=int(input("Enter The Number Of Student\n"))
	for i in range(number):
		id=int(input("Enter ID\n"))
		name=input("Enter The Name\n")
		address=input("Enter The Address\n")
	
		conn.execute("INSERT INTO student(id,name,address) VALUES (?,?,?)",(id,name,address))	

elif menu==2:
	select="SELECT * FROM student"
	cursor=conn.execute(select)
	print("The Student Details")

	i=1
	for c in cursor:	
		print("Student",i,":",c[0],c[1],c[2])
		i=i+1
conn.commit()
	
	