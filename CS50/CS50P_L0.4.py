# simple calculator using the float data type

# Practice 4 - floating-point arithmetic and rounding function
x = float(input("What's x? "))
y = float(input("What's y? "))

# round(number{, ndigits})
z = round(x + y)

print(z)

# Practice 5
x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y)

# numeric formatting where comma is added every triple of digits
# for example: 1,000
print(f"{z:,}")

# Practice 6 - round function format 1
x = float(input("What's x? "))
y = float(input("What's y? "))

# round(number{, ndigits}) 
# round result to one decimal point
z = round(x / y, 1)

print(z)

# Practice 7 - round function format 2
x = float(input("What's x? "))
y = float(input("What's y? "))

z = x / y

# round result to two decimal point
print(f"{z:.2f}")


