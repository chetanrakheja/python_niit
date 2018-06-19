sentence = input("enter a sentence \n")

'''
length_sen=len(sentence)
count=1
print()

for i in sentence:			#for counting no of words
	if i==" ":
		count+=1
	

print ("count =",count)	'''

words = sentence.split(" ")

print (words)
longestWord = ""
longestlen=0

i=0 
for j in words:
	if len(j)> longestlen:
		longestWord = j
		longestlen = len(j)
		
print("longest word is ",longestWord )
print("longest word length is ",longestlen )






