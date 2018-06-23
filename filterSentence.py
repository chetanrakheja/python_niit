sentence="my name is chetan rakheja i study in Jims vk"

excludedWords=['this','and' ,'is','in']
sentenceList = sentence.split(" ") 
print(sentenceList)
newSentenceList=[]

for i in sentenceList :
	if i not in excludedWords:
		newSentenceList.append(i)	



print(newSentenceList)