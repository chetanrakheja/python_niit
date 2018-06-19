sentence = input("enter a sentence \n")
#sentence = "tic tac toe is named as tic tac toe when it was made"

words = sentence.split(" ")

wordToSearch = input("enter a word to search \n")
#wordToSearch = "tic"

countWord=0

for j in words:
	if j==wordToSearch:
		countWord +=1
		


print (words)

print("NO of times",wordToSearch,"occured is",countWord)

# the below method also count words if occured in othe word
# like if we are searching for the it will also count the form there {(the)re}
'''
# OR
print()
countWord1 = sentence.count(wordToSearch)
print("2nd way")
print("NO of times",wordToSearch,"occured is",countWord1)

'''


