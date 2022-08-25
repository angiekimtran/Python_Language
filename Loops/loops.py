# this file contains examples of while and for loops

# new password set-up program
pw = input('Enter new password.')
pw2 = input('Re-enter new password.')

while pw != pw2:
    pw = input('Password does not match. Please re-enter password.')
    pw2 = input('Re-enter new password')
print('Congrats! New password is set.')

# flag program - enter stop to exit a program
flag = True

while flag:
  inputs = input ('Enter any words to display (enter STOP to exit)')
  if inputs == 'STOP': 
    flag = False
  print(inputs)

# program that prints all numbers divisible by 5 within 100
for i in range (101):
  if i % 5 == 0:
    print(i)