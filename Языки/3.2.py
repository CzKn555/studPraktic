num = int(input("Введите число: "))
str_num = str(num)
are_digits_unique = len(set(str_num)) == len(str_num)
print(are_digits_unique)