n = int(input())
n=n+1
lis=[]
for i in range(1,n):
    n=n-1
    if (n**2)%10==2 or (n**2)%10==5 or (n**2)%10==8:
        lis.append(n**2)
print(sum(lis))