def has_duplicates(L):
    seen = set()
    for element in L:
        if element in seen:
            return True
        seen.add(element)
    return False

L=input("enter: ")
print(has_duplicates(L))

'''
sample output 

enter: hello
True
'''
