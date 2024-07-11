year = int(input())
is_leap_year = "YES" if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else "NO"
print(is_leap_year)