#function
def x(a):
   print("Hello", a)
x('Mg Mg')
x('Ko Ko')

#lambda function
x=lambda a:a+20
print(x(5))

def myFunc(n):
    return lambda a:a*n

mydouble=myFunc(2)
print(mydouble(11))


#for loop
colors=('red', 'blue', 'green')
fruits=('orange', 'apple', 'banana')
for color in colors:
    for fruit in fruits:
        print(color, fruit)
