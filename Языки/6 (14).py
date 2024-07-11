m=int(input())
p=int(input())
n=int(input())
l=1
print(l,m)
for i in range(0,n-1):
    m=m*(1+p/100)
    l=l+1
    print(l, m)