a = float(input())
b = float(input())
c = float(input())
import math
d=b**2-4*a*c
if a!=0 or a!=b or a!=c:
    if d<0:
        print("нет корней")
    elif d==0:
        x1=-(b/2*a)
        print('\n', x1)
    elif d>0:
        x1=(-b+math.sqrt(d))/2*a
        x2=(-b-math.sqrt(d))/2*a
        print('\n', x1,'\n', x2)