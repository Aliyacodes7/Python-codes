import math
print("--word length--")
words=list(input("enter:").split(","))
print(words)
#counting word length
length=[]
for word in words:
    length.append(len(word))
print(length)
#taking average
average=sum(length)/len(words)
print(average)
#ceiling
roundoff=math.ceil(average)
print(roundoff)
#condition
comparator=[]
for num in length:
    if num>roundoff:
        comparator.append(num)
print(comparator)
#count
count=0
for num in comparator:
    count+=1
print(count)

'''
sample output 
--word length--
enter: apple,banana,kiwi,grape,blueberry
['apple', 'banana', 'kiwi', 'grape', 'blueberry']
[5, 6, 4, 5, 9]
5.8
6
[9]
1
'''
