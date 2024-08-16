'''
a = float(input("Enter first number = "))
b = float(input("Enter second number = "))
print(" press 1 for add \n press 2 for sub \n press 3 for mul \n press 4 for div")
input=int(input("Enter choice from 1-4 = " ))

if input ==1:
    print(a+b)
    
elif input ==2:
    print(a-b)
elif input == 3:
    print(a*b)
elif input==4:
    print(a/b)
else:
    print("enter correct number ")
    '''
def cal  (a,n):
    print(" press 1 for add \n press 2 for sub \n press 3 for mul \n press 4 for div")
    input=int(input("Enter choice from 1-4 = " ))

    if input ==1:
       print(a+b)
    
    elif input ==2:
        print(a-b)
    elif input == 3:
        print(a*b)
    elif input==4:
         print(a/b)
    else:
        print("enter correct number ")
        return input
a = float(input("Enter first number = "))
b = float(input("Enter second number = "))
cal(a,b)