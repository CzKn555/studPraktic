n = int(input())
lis=[]
for i in range(1,n):
    if n%i==0:
        lis.append(i)
print(sum(lis))
print(lis)