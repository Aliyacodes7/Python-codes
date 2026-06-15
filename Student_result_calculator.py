print("student result calculator")
try:
    print("file opened")
    marks1=int(input("enter marks of sub 1: "))
    marks2=int(input("enter marks of sub 2: "))
    marks3=int(input("enter marks of sub 3: "))
    total=marks1+marks2+marks3
    print("total marks out of 300:", total)
    percentage=(total/300)*100
    print("the percentage is:", percentage)
    if percentage>=75:
        print("grade a")
    elif percentage>=60:
        print("grade b")
    elif percentage>=35:
        print("grade c")
    else:
        print("fail")

except ValueError:
    print("invalidvalue")
except Exception as e:
    print(e)

finally:
    input()


'''
student result calculator
file opened
enter marks of sub 1: 75
enter marks of sub 2: 65
enter marks of sub 3: 80
total marks out of 300: 220
the percentage is: 73.33333333333333
grade b
'''
