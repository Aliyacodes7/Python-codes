import random
fruits=["apple","grape","mango"]
picked_fruit=random.choice(fruits)
display="_ "*len(picked_fruit)
print(display)
#game variable
guess_letters =[]
attempt=5
while attempt > 0:
    guess_letter=input("\nEnter letter : ")
    print(guess_letter)
    guess_letters.append(guess_letter)
    for letter in picked_fruit:
        if letter in guess_letters:
            print(letter , end=" ")
        else:
            print("_", end=" ")
    if guess_letter not in picked_fruit:
        attempt -= 1
        print("\nWrong! Attempts left : ", attempt)
    # Check if won
    all_guessed = True
    for letter in picked_fruit:
        if letter not in guess_letters:
            all_guessed = False
    if all_guessed:
        print("\n correct")
        break

  '''
  sample output when mango is randomly chosen
  
_ _ _ _ _

Enter letter : m
m
m _ _ _ _

Enter letter : g
g
m _ _ g _

Enter letter : l
l
m _ _ g _

Wrong! Attempts left : 4

Enter letter : a
a
m a _ g _

Enter letter : n
n
m a n g _

Enter letter : o
o
m a n g o

correct
'''
