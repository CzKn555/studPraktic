data = int(input())
if(data <= 13):
    print('детство')
elif(data >= 14 and data <= 24):
    print('молодость')
elif(data >= 25 and data <= 59):
    print('зрелость')
else:
    print('старость')