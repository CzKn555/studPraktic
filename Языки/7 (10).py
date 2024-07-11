import math
n=int(input())
lis=[]
for i in range(1,n):
    lis.append(n)
    n=n-1
print(math.prod(lis))