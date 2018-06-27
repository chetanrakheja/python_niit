#sentence = input("enter a sentence \n")
sentence = "tic tac toe is named as tic tac toe when it was made"
sentenceList = sentence.split(" ") 

print(sentenceList)
sortedSentenceList=sentenceList.copy()
sortedSentenceList.sort()

dict1={}
for i in sortedSentenceList:
	a=i
	dict1[a]=sentenceList.count(a)
	
print()
print()
print()

print(dict1)

for x in keys_list:
	print(x,d[x])