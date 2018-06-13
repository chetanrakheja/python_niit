a=[]

for i in range(1,11):
	print("enter input",i)
	a.append(int(input()))

smallest=a[0]	
largest=a[0]	
for i in range(0,10):
	if(smallest>a[i]):
		smallest=a[i]
		
	if (largest<a[i]):
		largest=a[i]
		
	
	
print(a)
print("smallest is ",smallest)
print("largest is ",largest)
	
