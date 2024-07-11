num = int(input())
is_four_digit = 1000 <= num <= 9999
is_divisible_by_7_or_17 = num % 7 == 0 or num % 17 == 0
is_beautiful = is_four_digit and is_divisible_by_7_or_17
result = "YES" if is_beautiful else "NO"
print(result)