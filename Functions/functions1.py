# this program contains useful python functions
# remember that braces look like { } and are used for list notation.
# parentheses look like ( ) and are used in interval notation when an endpoint IS NOT included.
# brackets look like [ ] and are used in interval notation when an endpoint IS included.

# zip()
products = ["apple", "banana", "pear"]
counts = [6, 20, 11]

for product, count in zip(products, counts):
  print(product, count)
# zip() interates two lists simultaneously

# type()
print(type(counts))
# type() tells you what kind of type a variable is

my_list = [23, 54, 12, 74,39, 58, 23, 74, 23]

# sum()
print(sum(my_list))
print(type(sum(my_list)))
# sum() sums together a list of elements

# set()
print(set(my_list))
print(type(set(my_list)))
# set() shows all the unique elements in a list

# list()
print(list(set(my_list)))
print(type(list(set(my_list))))
# list() can convert an interval into a list

# sorted()
print(sorted(my_list))
# sorted() sorts the elements in a list

# min() and maz()
print(min(my_list))
print(max(my_list))
# the min() and max() functions helps us find the smallest and largest element in a list

# range()
print(range(10))
print(list(range(10)))
for i in range(10):
    print(i)
# range() is an interval and generates a range of elements

# round()
pi = 3.1415
print(round(pi, 2))
# round() function is often used when rounding a float
# the above example rounds pi to two decimal points