aString = 'Hello, World!'
res = False
#aString = 'hello'
res = aString.capitalize()
res = aString.casefold()
res = aString.center(80)
res = aString.count('o')
res = aString.encode()
res = aString.endswith('!')
#aString = 'h\te\tl\tl\to'
res = aString.expandtabs(2)
res = aString.find('o')
#aString = 'Hello, {}'
res = aString.format('Javi')
res = aString.index('o')
#aString = '12345678'
res = aString.isalnum()
#aString = 'abcdefgh'
res = aString.isalpha()
res = aString.isdecimal()
res = aString.isdigit()
#aString = 'Hi'
res = aString.isidentifier()
#aString = 'hello'
res = aString.islower()
res = aString.isnumeric()
res = aString.isprintable()
#aString = ''
#aString = ' '
res = aString.isspace()
res = aString.istitle()
#aString = 'HELLO'
res = aString.isupper()
res = '#'.join(aString)
res = aString.ljust(16)
#print(res, '...is cool')
res = aString.lower()
#aString = '        Hi        '
res = aString.lstrip()
res = aString.maketrans('H', 'J')
# print(aString.translate(res))
res = aString.partition(',')
res = aString.replace(',', '#')
res = aString.replace('World', 'Javi')
res = aString.rfind('o')
res = aString.rindex('o')
res = aString.rjust(16)
res = aString.rpartition(',')
res = aString.rsplit(',')
res = aString.rstrip()
res = aString.split(',')
res = aString.splitlines()
res = aString.startswith('H')
#aString = '        Hi        W'
res = aString.strip()
res = aString.swapcase()
#aString = 'hello, world!'
res = aString.title()
res = aString.upper()
res = aString.zfill(16)
print(res)
