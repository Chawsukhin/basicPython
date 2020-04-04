if input() == '1234':
    print('Your password is correct.')
else:
    print('Your password is incorrect.')

x='a'
if x=='a':
   print('Hello')
   print('_'*52)

x=input('Enter yes or no :')
if x=='yes':
    print('Hello World')
elif x=='no':
    print('Error')

x=input('Enter yes or no or other words:')
if x=='yes':
    print('Yes, Hello World')
elif x=='no':
    print('No, Error')
else:
    print('Other words')


x=input("yes (to continue) / no (to stop)\n Enter:")
while x=='yes':
    print("while statement can run non stop")


x='yes'
while x=='yes':
    x=input("yes (to continue) / no (to stop)\n Enter:")
