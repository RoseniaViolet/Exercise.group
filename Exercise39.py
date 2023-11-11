decibels = int(input('Enter the number of decibels: '))
if decibels == 130:
    print('Jackhammer')
elif decibels == 106:
    print('Gas lawnmower')
elif decibels == 70:
    print('Alarm clock')
elif decibels == 40:
    print('Quiet room')
elif 40 < decibels < 70:
    print('Between a Quiet room and an Alarm clock')
elif 70 < decibels < 106:
    print('Between an Alarm clock and a Gas lawnmower')
elif 106 < decibels < 130:
    print('Between a Gas lawnmower and a Jackhammer')
elif decibels < 40:
    print('Too low to be audible')
elif decibels > 130:
    print('Too high to be audible')
else:
    print('Invalid decibel level')

