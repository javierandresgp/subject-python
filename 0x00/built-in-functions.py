a = -8.42
b = [True, True, True, True]
c = [False, False, True, False]
d = "My name is Ståle"
e = 8


def f():
    x = 4


g = 72


class Person:
    name = 'Javi'
    age = 44


h = ('apple', 'banana', 'cherry')
i = 'print(8)'
j = 'name = "Javi"\nprint(name)'
k = 0.19
l = ['apple', 'banana', 'cherry']

res = abs(a)  # Returns the absolute value of a number
res = all(b)  # Returns True if all items in an iterable object are true
res = any(c)  # Returns True if any item in an iterable object is true
res = ascii(d)  # Replaces none-ascii characters with escape character
res = bin(e)  # Returns the binary version of a number
res = bool(e)  # Returns the boolean value of the specified object
res = bytearray(e)  # Returns an array of bytes
res = bytes(e)  # Returns a bytes object
res = callable(f)  # Returns True if the specified object is callable
res = callable(e)  # otherwise return False
res = chr(g)  # Returns a character from the specified Unicode code.
res = complex(e, g)  # Returns a complex number
res = delattr(Person, 'age')  # Deletes the specified attribute
res = dict(name='Javi', age='44')  # Returns a dictionary
res = dir(Person)  # Returns a list of the specified object
res = divmod(g, e)  # Return the quotient and the remainder of g divided by e
res = list(enumerate(h))  # Returns it as an enumerate object
res = eval(i)  # Evaluates and executes an expression
res = exec(j)  # Executes the specified code (or object)
res = float(g)  # Returns a floating point number
res = format(k, '%')  # Formats a specified value
res = frozenset(l)  # Returns a frozenset object
res = globals()  # Returns the current global symbol table as a dictionary
print(res)
# classmethod()	Converts a method into a class method
# compile()	Returns the specified source as an object, ready to be executed
# filter(function, iterable) Use a filter function to exclude items in an iterable object
# getattr() Returns the value of the specified attribute
