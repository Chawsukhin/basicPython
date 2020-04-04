# standard library function

from math import sqrt
import math

data=int(input("Enter a number to square root"))
print("The square root of{} is{}".format(data,sqrt(data)))

print("The value of pi",math.pi)
print("The exp of {} is {}".format(data,math.exp(data)))

# programmer defined function

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multi(a,b):
    return a*b

def div(a,b):
    return a/b

data1=int(input("Enter a first number:"))

data2=int(input("Enter a second number:"))
print("Adding",add(data1,data2))
print("Subtraction",sub(data1,data2))
print("Multi",multi(data1,data2))
print("Division",div(data1,data2))
