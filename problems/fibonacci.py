a=int(input("enter number= "))
b=0
c=1
if a>0:
    print(b)
    print(c)
    for i in range(2,a):
        d=b+c
        b=c
        c=d
        print(d)