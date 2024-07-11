a = int(input())
b = int(input())
s=0
while a<=b:
    
    t=a**3
    a=a+1
    if t%10==4 or t%10==9:
        s=s+1
print(s)        