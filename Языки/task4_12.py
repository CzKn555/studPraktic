num = int(input())

if 0 < num < 4:
    print("I" * num)

elif 3 < num < 9:
    print(((5 - num) * "I") + "V" + ((num - 5) * "I"))

elif 8 < num < 13:
    print(((10 - num) * "I") + "X" + ((num - 10) * "I"))