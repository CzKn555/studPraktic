m = int(input())
n = int(input())
m=m+1
while m>n+1:
    k=m%2
    m=m-(1+k)
    print(m)