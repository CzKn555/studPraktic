number = input("Введите число: ")

digit_1 = int(number[0])
digit_2 = int(number[1])
digit_3 = int(number[2])

max_digit = digit_1
min_digit = digit_1

if digit_2 > max_digit:
    max_digit = digit_2
elif digit_2 < min_digit:
    min_digit = digit_2

if digit_3 > max_digit:
    max_digit = digit_3
elif digit_3 < min_digit:
    min_digit = digit_3

sum_digits = digit_1 + digit_2 + digit_3 - max_digit - min_digit
middle_digit = sum_digits

if max_digit - min_digit == middle_digit:
    print("Число интересное")
else:
    print("Число неинтересное")
