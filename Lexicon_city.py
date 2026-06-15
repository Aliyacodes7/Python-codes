print("--lexicon city--")
message=list(input("enter words: ").split(","))
print(message)
#to print word of min length
minlength=message[0]
for word in message:
    if len(word)<=len(minlength):
        minlength=word
print(minlength)

'''
sample output 
--lexicon city--
enter words: apple,banana,kiwi,grape
['apple', 'banana', 'kiwi', 'grape']
kiwi
'''
