#sentence = input("enter a sentence \n")
sentence = "tic tac toe is named as tic tac toe when it was made"
b=[]

excludedWords=['this','and' ,'is','in']
sentenceList = sentence.split(" ") 
print(sentenceList)
newSentenceList=[]

for i in sentenceList :
	if i not in excludedWords:
		newSentenceList.append(i)	

print(newSentenceList)
newSentenceListLength=len(newSentenceList)

for i in newSentenceList :
	if i not in b:
		b.append(i)	
print(b)

for i in b:
	a=i
	print(a,round((newSentenceList.count(a)/newSentenceListLength),3))

