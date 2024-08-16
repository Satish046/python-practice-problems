
a = int (input("enter number to find factoriral = "))
#num = 1
if a<0 :
    print("facorial dosent exist ")
if a==0:
    print("factorial of 0 is 1")
             
if a>0 :
    num = 1
    for i in range(1,a+1):
        num=num*i
print("factorial =",num)


#or
import math

num = int(input("enter value ="))
result = math.factorial(num)

print(f"The factorial of {num} is {result}")

#finding factors
fact=int(input("Enter number to find factors = "))
for i in range (1,fact+1):
    if fact % i == 0:
        print(i)


        