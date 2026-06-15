print("--temperature alert system--")
readings=list(map(int , input("enter temp:").split()))
print(readings)
alert=[]
for values in readings:
    if values>50:
        alert.append(str(values))
if len(alert)==0:
    print("0")
else:
    print(" ".join(alert))

'''  
sample output
--temperature alert system--
enter temp: 45 55 60 40 70
[45, 55, 60, 40, 70]
55 60 70
'''
