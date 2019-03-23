Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 23 2018, 23:31:17) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print(abs(10))
10
>>> print(abs(-10))
10
>>> steps = -3
>>> is abs(steps) > 0:
	
SyntaxError: invalid syntax
>>> steps = -3
>>> if abs(steps) > 0:
	print('Character is moving')

	
Character is moving
>>> steps = -3
>>> if steps < 0 or steps > 0:
	print('Character is moving')

	
Character is moving
>>> print(bool(0))
False
>>> print(bool(1))
True
>>> print(bool(1123.23))
True
>>> print(bool(-500))
True
>>> print(bool(None))
False
>>> print(bool('a'))
True
>>> print(npp;s(' '))
SyntaxError: invalid syntax
>>> print(bool(' '))
True
>>> print(bool('What do you call a pig doing karate? Pork Chop!'))
True
>>> my_silly_list = []
>>> print(bool(my_silly_list))
False
>>> my_silly_list = ['s', 'i', 'l', 'l', 'y']
>>> print(bool(my_silly_list))
True
>>> year = input ('Year of birth: ')
Year of birth: 
>>> if not bool (year.rstrip()):
	print('You need to enter a value for your year of birth')

	
You need to enter a value for your year of birth
>>> 
>>> 
>>> dir(['a', 'short', 'list'])
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> dir(1)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> popcorn = 'Ilove popcorn!'
>>> dir(popcorn)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help(popcorn.upper)
Help on built-in function upper:

upper(...) method of builtins.str instance
    S.upper() -> str
    
    Return a copy of S converted to uppercase.

>>> 
>>> 
>>> eval('10*5')
50
>>> eval('''if True:
	print("this won't work at all")''')
Traceback (most recent call last):
  File "<pyshell#42>", line 2, in <module>
    print("this won't work at all")''')
  File "<string>", line 1
    if True:
     ^
SyntaxError: invalid syntax
>>> your_calculation = input('Enter a calculation:')
Enter a calculation:eval(your_calculation)
>>> your_calculation = input('Enter a calculation:')
Enter a calculation:12*52
>>> eval(your_calculation)
624
>>> 
>>> 
>>> my_small_program = '''print('ham')
    print('sandwhich')'''
>>> exec(my_small_program)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    exec(my_small_program)
  File "<string>", line 2
    print('sandwhich')
    ^
IndentationError: unexpected indent
>>> my_small_program = '''print('ham')
print('sandwhich')'''
>>> exec(my_small_program)
ham
sandwhich
>>> 
>>> 
>>> 
>>> float('12')
12.0
>>> float ('123.456789')
123.456789
>>> 
>>> 
>>> your_age = input('Enter your age:')
Enter your age:20
>>> age = float(your_age)
>>> if age > 13:
	print('You are %s years too old' % (age -13))

	
You are 7.0 years too old
>>> 
>>> 
>>> int('123')
123
>>> int ('123.456')
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    int ('123.456')
ValueError: invalid literal for int() with base 10: '123.456'
>>> len('this is a test string')
21
>>> creature_list = ['unicorn', 'cyclops', 'fairy', 'elf', 'dragon', 'troll']
>>> print(len(creature_list))
6
>>> enemies_map {'Batman' : 'Joker', 'Superman' : 'Lex Luthor', 'Spiderman' : 'Green Goblin'.}
SyntaxError: invalid syntax
>>> enemies_map = {'Batman' : 'Joker', 'Superman' : 'Lex Luthor', 'Spiderman' : 'Green Goblin'}
>>> print(len(enemies_map))
3
>>> fruit = ['apple', 'banana', 'clementine', 'dragon fruit']
>>> length = len(fruit)
>>> for x in range(0, length):
	print('the fruit at index %s is %s' % (x, fruit[x]))

	
the fruit at index 0 is apple
the fruit at index 1 is banana
the fruit at index 2 is clementine
the fruit at index 3 is dragon fruit
>>> 
>>> 
>>> numbers = [5, 4, 10, 30, 22]
>>> print(max_numbers))
SyntaxError: invalid syntax
>>> print(max(numbers))
30
>>> strings = 's,t,r,i,n,g,S,T,R,I,N,G'
>>> print(max(strings))
t
>>> print(max(10,300,450,50,90))
450
>>> numbers = [5, 4, 10, 30, 22]
>>> print)min(numbers))
SyntaxError: invalid syntax
>>> print(min(numbers))
4
>>> guess_this_numbers = 61
>>> player_guesses = [12, 15, 70, 45]
>>> if max(player_guesses) > guess_this_number:
	print('Boom! You all lose')
else:
	print:('You win')

	
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    if max(player_guesses) > guess_this_number:
NameError: name 'guess_this_number' is not defined
>>> guess_this_number = 61
>>> player_guesses = [12, 15, 70, 45]
>>> if max(player_guesses) > guess_this_number:
	print('Boom! You all lose')
else:
	print('You win')

	
Boom! You all lose
>>> 
>>> 
>>> 
>>> for x in range (0,5):
	print(x)

	
0
1
2
3
4
>>> print(list(range(0,5))))
SyntaxError: invalid syntax
>>> print(list(range(0,5)))
[0, 1, 2, 3, 4]
>>> count_by_twos = list(range(0,30,2))
>>> print(count_by_twos)
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
>>> countdown_by_twos = list(range(40,10,-2))
>>> print(count_down_by_twos)
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    print(count_down_by_twos)
NameError: name 'count_down_by_twos' is not defined
>>> count_down_by_twos = list(range(40,10,-2))
>>> print(count_down_by_twos)
[40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12]
>>> my_list_of_numbers = list(range(0,500,50))
>>> print(my_list_of_numbers)
[0, 50, 100, 150, 200, 250, 300, 350, 400, 450]
>>> print(sum(my_list_of_numbers))
2250
>>> 
