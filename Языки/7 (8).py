import math
n = int(input())
s =n
t=n
lis = []
lis2=[1]
lis3=[]
while n>0:
    c = n%10
    n=n//10
    lis.append (c)
r =len(lis)
while s>0 and r>0:
    l=10**r+s
    s=s-1
    lis2.append(l)
    while s>0:
        g = s%10
        lis3.append (g)
        if s>=10:
            s=s//10
        elif s<10:
            break
        break
        
    r =len(lis3)
    lis3.clear()
ch= math.log(t)
p=sum(lis2)-ch
print(p)
print(lis2)
