# practice program of useful functions in python

# map() return string of x element
def my_func(x):
    return 'x'*x

x_list = map(my_func, [1, 2, 3, 4, 5])
print(list(x_list))


# map() return double of n
def addition(n):
    return n + n
  
numbers = (1, 2, 3, 4, 5)
result = map(addition, numbers)

print(list(result))

# map() return length of each word in the tuple
# tuple
def myfunc(n):
  return len(n)

x = map(myfunc, ('orange', 'stawberry', 'pear'))
print(list(x))

# tuple vs list
l = [1,2,3]
print(tuple(l))

# isinstance() return instances of string data type in list
new_list = ['hello', 2, 5.9, 'world', 'hello world']

strings = [item for item in new_list if isinstance(item, str)]
print(strings)