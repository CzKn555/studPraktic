m = int(input())
n = int(input())
while m<=n:
    m=m+1
    if m%17==0 or m%10==9 or (m%3==0 and m%5==0):
        print(m)