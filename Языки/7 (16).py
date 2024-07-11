n=int(input())
lis=[1,1]
l=1
i=1
if n<=100:
    while len(lis)<=n:
        r=i
        i=i+l
        l=r
        lis.append(i)
for i in (lis):
    print(i, end=" ")
