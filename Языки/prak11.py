data1 = int(input())
print(data1 // 2 + data1 % 2)
uslovie = [int(data1 / 2), data1 - int(data1 / 2)]
print(uslovie[data1 % 2])