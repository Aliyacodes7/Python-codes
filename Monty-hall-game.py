import random
doors=["1","2","3"]
display="█"*3
print("doors:",display)
gold=random.choice(range(1,4))
print("gold door:",gold)
user=int(input("enter choice: "))
print("your choice:",user)
#eliminate one Empty door after user choice
possible_doors = []
for door in doors:
    if door!=str(user) and door!=str(gold):
        possible_doors.append(door)
eliminated_door = random.choice(possible_doors)
print("Door eliminated:",eliminated_door)
#option for swap
swap=input("Do you want to change your choice? \n Enter 1 to change and 2 for no change: ")
if (swap==1):
    if doors[user]==str(gold):
        print("win")
    else:
        print("lose")
else: #when swap==2
    if doors[user]==str(gold):
        print("lose")
    else:
        print("win")

  '''
  sample output

  doors: ███
gold door: 3 (randomly chosen gold door)
enter choice: 1
your choice: 1
Door eliminated: 2
Do you want to change your choice?
Enter 1 to change and 2 for no change: 1
win
'''
