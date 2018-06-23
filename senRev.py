sentence="a cat ran"

words = sentence.split(" ")
print(words)
words=words[-1::-1]
print(words)
newSentence=" ".join(words)
print(newSentence)