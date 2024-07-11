x = int(input("Введите число: "))
if -30 < x <= -2 or 7 < x <= 25:
    belongs_to_interval = "Принадлежит"
else:
    belongs_to_interval = "Не принадлежит"
print(belongs_to_interval)