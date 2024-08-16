
#n=int(input("enter number = "))
#m=int (input("enter number = "))

def hcf(n,m):
    
    if n>m:
        smaller=m
    else:
         smaller=n
    for i in range(1,smaller+1):
        if ((n%i==0) and (m%i==0)):
            gcd=i
    return gcd
n=int(input("enter number = "))
m=int (input("enter number = "))
result=hcf(n,m)
print(result)