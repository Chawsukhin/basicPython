x="nothing forever"
y=x.capitalize()
print(y)

x="Hello World"
y=x.casefold()
print(y)

x="hello world"
y=x.center(19,'*')
print(y)

x="Nothing is forever. We can change the future."
y=x.count('e')
print(y)

x="Nothing is forever. We can change the future."
y=x.count('e',0,15)
print(y)

x="I Love Python."
y=x.endswith("Python.")
print(y)

x="Hello\tWorlds"
y=x.expandtabs(20)
print(y)

x="Hello World"
y=x.find('l')
print(y)


x="Hello World"
y=x.index('l')
print(y)

x="Hello {}. Nice to meet you."
print(x.format(input('What is your name?\n Answer\t')))


x="Hello {a}. Nice to meet you."
y=x.format_map({'a': 'mg mg'})
print(y)

x="HelloWorld2"
y=x.isalnum()
print(y)

x="Hello World *"
y=x.isalpha()
print(y)

x="12345"
y=x.isdecimal()
print(y)

x="1011000"
y=x.isdigit()
print(y)

x="air"
y=x.isidentifier()
print(y)

x="idontcare 123"
y=x.islower()
print(y)

x="\u00bd"
print(x)
y=x.isnumeric()
print(y)

x=chr(27)
y=x.isprintable()
print(y)

x="     "
y=x.isspace()
print(y)

x="Hello World"
print(type(x))

x={"name":"John", "age":36}
print(x)

x={"apple", "banana", "cherry"}
print(x)

x=frozenset({"apple", "banana", "cherry"})
print(x)

x=frozenset({1, 100, 50})
print(x)
