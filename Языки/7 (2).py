m = int(input())
n = int(input())
if m<n:
    m=m-1
    while m<n:
        m=m+1
        print(m)
elif m>n:
    m=m+1
    while m>n:
        m=m-1
        print(m)