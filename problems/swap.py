#without using third value or temp
a = 5
b = 25
a,b = b,a
print("a is = ",a)
print("b is = ",b)
 # with using temp
a=11
b=22
temp=a
a=b
b=temp
print("a is = ",a)
print("b is = ",b)