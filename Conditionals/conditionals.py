#Below are programs that demonstrate Python's if-else and elif conditionals

# This program ask users to input an integer, then checks whether the integer is an even number or an odd number
x = int(input('Enter an integer:'))
if x%2  == 0:
  print('Even number')
else:
  print('Odd number')

# This program  tells users the ideal weather to go out in Colorado
# According to google, the ideal temp in Colorado is 65 - 85 degrees Fahrenhiet
temp = float(input('Enter the temperature of today in Fahrenhiet: '))

if temp > 85:
  print('Wow! That\'s too hot!')
elif temp < 65:
  print('OMG! That\'s so cold!')
else:
  print('Perfect temperature to go out!')