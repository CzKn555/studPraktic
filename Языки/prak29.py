data1 = int(input())
data2 = int(input())
data3 = int(input())
data4 = list()
if(data1 > 0):
    data4.append(data1)
if(data2 > 0):
    data4.append(data2)
if(data3 > 0):
    data4.append(data3)
print(sum(data4)) if len(data4) != 0 else print(0)