import random
action=["rock","paper","scissors"]
bot=random.choice(action)
print(bot)
human=input("enter action: ")
if bot==human:
    print("draw")
elif bot=="rock" and human=="paper":
    print("win")
elif bot=="rock" and human=="scissors":
    print("lose")
elif bot=="paper" and human=="rock":
    print("lose")
elif bot=="paper" and human=="scissors":
    print("win")
elif bot=="scissors" and human=="rock":
    print("win")
elif bot=="scissors" and human=="paper":
    print("lose")

'''
sample output
rock (when bot chosen rock)
enter action: paper
win
'''
