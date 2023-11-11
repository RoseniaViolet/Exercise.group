Par_value = int(input('Enter the denomination of a banknote: $'))
name =''
if Par_value == 1:
     name = "George Washington"
elif Par_value == 2:
     name = 'Thomas Jefferson'
elif Par_value == 5:
     name = 'Abraham Lincoln'
elif Par_value == 10:
     name = 'Alexander Hamilton'
elif Par_value == 20:
     name = 'Andrew Jackson'
elif Par_value == 50:
     name = 'Ulysses S. Grant'
elif Par_value == 100:
     name = 'Benjamin Franklin'
else:
     name = ''
if name:
    print(f"${Par_value} banknote has an image of {name}")
else:
    print("No such note exists!")