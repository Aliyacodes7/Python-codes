print("--Energy readings--")
reading=list(map(int , input("Enter readings:").split()))
print(reading)
#summation of values in the list
total=0
for num in reading:
    total=total + num
print(total)
divide=total/len(reading)
#condition
values=[]
for num in reading:
    if num>divide:
        values.append(num)
print(values)
#to count values
count=0
for num in values:
    if num>divide:
        count=count+1
print(count)

'''
sample output
--Energy readings--
Enter readings: 10 20 30 40 50
[10, 20, 30, 40, 50]
150
[40, 50]
2
'''
