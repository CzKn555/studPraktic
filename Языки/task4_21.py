
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())

minimum = num1
maximum = num1

if num2 < minimum:
    minimum = num2
if num3 < minimum:
    minimum = num3
if num4 < minimum:
    minimum = num4
if num5 < minimum:
    minimum = num5

if num2 > maximum:
    maximum = num2
if num3 > maximum:
    maximum = num3
if num4 > maximum:
    maximum = num4
if num5 > maximum:
    maximum = num5

print("Наименьшее число:", minimum)
print("Наибольшее число:", maximum)
