sentence = input("Write a sentence: ")
punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
for i in sentence:
    if i in punctuation:
        sentence = sentence.replace(i, "")
spaces = sentence.split()
wordcount = len(spaces)
stringlength = len(sentence)
reversestring = sentence[stringlength::-1]

print("There are " + str(wordcount) + " words in the sentence.")
print("The reverse of the sentence is:\n" + reversestring)
