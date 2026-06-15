L=[55,56,57,58,59,60,61,62,63]

def safe_first(L):
    if not L:
        return None
    return L[0]

def safe_last(L):
    if not L:
        return None
    return L[-1]

def safe_middle(L):
    if not L:
        return None
    if len(L) <= 2:
        return []
    return L[1:-1]

print(safe_first(L))
print(safe_last(L))
print(safe_middle(L))

'''
sample output 
55
63
[56, 57, 58, 59, 60, 61, 62]
'''
