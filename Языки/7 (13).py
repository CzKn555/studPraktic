n = int(input())
lis=[]
for i in range(1,n+1):
    if i%2==0:
        r=i*(-1)
        lis.append(r)
    elif i%2!=0:
        m=i
        lis.append(m)
print(sum(lis))
print(lis)