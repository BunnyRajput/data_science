def square(x):
    return x*x
print(square(5))

def sum_of_square(x,y):
    return square(x) + square(y)
print(sum_of_square(2,3))

x = 1
def f():
    return x
print (x)
print (f())

x = 1
def f():
    x = 2
    return x
print (x)
print (f())
print (x)



x = 1
def f():
    
    x = 2
    y = x
    return x + y
print(x)
print(f())
print(x)

x = 2
def f(a):
    x = a * a
    return x
y = f(3)
print (x, y)

def difference(x ,y):
    return x - y
print(difference(5,6))
print(difference(x = 5, y= 4))
#Write a function count_digits to find number of digits in the given number.
def countdigit(n):
    count = 0
    while n != 0: 
        n //= 10
        count+= 1
    return count 
print(countdigit(123456789))

x = "hello"
print(x.upper())

#Write a function istrcmp to compare two strings, ignoring the case
def strcompari(x,y):
    if x == y:
        print("both are same")
    else:
        print("both are not equall")
print (strcompari("hello","hi"))        


x = 2
if x == 2:
    print (x)
else:
    print (y)


x = [1,2,3]
print(x)

x = [1, 2, "hello", "world", ["another", "list"]]
print(x)

import time
print(time.asctime())

x = [1, 2, 3, 4]
print(x[0:-1])
x = [0, 1, [2]]
x[2][0] = 3
print(x)
x[2].append(4)
print (x)
x[2] = 2
print (x)

