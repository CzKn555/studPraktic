n = int(input())
lis=[]
if n>=2:
    for i in range(0,n):
        a = int(input())
        lis.append(a)
d=max(lis)
lis.remove(d)
r=max(lis)
print(d)
print(r)