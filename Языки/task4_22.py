num1 = int(input())
num2 = int(input())
num3 = int(input())

max_num = num1
min_num = num1
mid_num = num1

if num2 > max_num:
    max_num = num2
elif num2 < min_num:
    min_num = num2
else:
    mid_num = num2

if num3 > max_num:
    max_num = num3
elif num3 < min_num:
    min_num = num3
else:
    mid_num = num3

if num1 != max_num and num1 != min_num:
    mid_num = num1
elif num2 != max_num and num2 != min_num:
    mid_num = num2
else:
    mid_num = num3

print(max_num, mid_num, min_num)
