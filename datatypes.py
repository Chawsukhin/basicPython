x=str("Hello World")
print(type(x))
print(x)

x=int(20)
print(type(x))
print(x)

x=float(10.5)
print(type(x))
print(x)

x=complex(1j)
print(type(x))
print(x)

x=list(("apple", "banana", "orange"))
print(type(x))
print(x)

x=tuple(("apple", "banana", "orange"))
print(type(x))
print(x)

x=range(6)
print(type(x))
print(x)


x=dict(name="John", age=36)
print(type(x))
print(x)

x=set(("apple", "banana", "orange"))
print(type(x))
print(x)

x=frozenset(("apple", "banana", "orange"))
print(type(x))
print(x)

x=bool(6)
print(x)

x=bytes(8)
print(x)

x=bytearray(5)
print(x)


x=memoryview(bytes(5))
print(x)
