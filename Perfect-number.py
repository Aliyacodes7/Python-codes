def is_perfect(n):
    try:
        divide=[]
        for i in range(1,n):
            if n%i==0:
                divide.append(i)
        print(divide)
        if sum(divide)==n:
            return True
        return False
    except (ValueError):
        print("enter positive integer only")
        return False

n=int(input("enter positive value:"))
result=is_perfect(n)
print(result)

'''
sample output 
enter positive value: 28
[1, 2, 4, 7, 14]
True
'''
