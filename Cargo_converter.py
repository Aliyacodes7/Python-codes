print("--cargo weight--")
weight=list(input("enter: ").split())
print(weight)
#using loop
cargo=[]
for value in weight:
    cargo.append(str(int(float(value))))
print(cargo)

'''
sample output 
--cargo weight--
enter: 12.5 8.3 20.7 15.0
['12.5', '8.3', '20.7', '15.0']
['12', '8', '20', '15']
'''
