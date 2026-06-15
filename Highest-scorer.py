def student():
    #created a dictionary
    dictionary = {
        "1": {"Name": "A", "marks": [20,10]},
        "2": {"Name": "B", "marks": [15,5]}
    }
    print(f"record: {dictionary}")
    #finding the one with highest marks altogether
    t=[]
    for key in dictionary:
        total=sum(dictionary[key]["marks"])
        t.append(total)
        print(dictionary[key]["Name"], total)
    #printing the highest one
    print(f"Highest scorer:",max(t))
student()

'''
sample output 

record: {'1': {'Name': 'A', 'marks': [20, 10]}, '2': {'Name': 'B', 'marks': [15, 5]}}
A 30
B 20
Highest scorer: 30
'''
