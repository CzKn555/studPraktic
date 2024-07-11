x = int(input("Введите число: "))
y = int(input("Введите число: "))
if x > 0 and y > 0:
    quadrant = 1
elif x < 0 and y > 0:
    quadrant = 2
elif x < 0 and y < 0:
    quadrant = 3
elif x > 0 and y < 0:
    quadrant = 4
else:
    quadrant = "Точка находится на оси координат"
print("Номер координатной четверти:", quadrant)