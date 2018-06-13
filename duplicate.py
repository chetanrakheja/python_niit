a=[1,2,3,4,5,6,56,3,1,2] 
b=[]
for i in range(0,10):
	if a[i] not in b:
		b.append(a[i])
		
print("a is ",a)
print("b is ",b)