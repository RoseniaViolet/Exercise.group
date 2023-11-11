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
    print('Quieter than an alarm clock')
elif 70 < decibels < 106:
    print('Quieter than a gas lawnmower')
elif 106 < decibels < 130:
    print('Quieter than a jackhammer')
elif decibels < 40:
    print('Too low to audible')
else:
    print('Too high to audible')
