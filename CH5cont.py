Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 23 2018, 23:31:17) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> if age == 10 or age == 11 or age == 12 or age == 13:
	print('What is 13 + 49 + 84 + 155+ 97? A headache!')
else:
	print('Huh?')

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    if age == 10 or age == 11 or age == 12 or age == 13:
NameError: name 'age' is not defined
>>> if age >=10 and age <= 13:
	print ('What is 13 + 49 + 84 + 155 + 97? Headache!')
else:
	print('Huh?')

	
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    if age >=10 and age <= 13:
NameError: name 'age' is not defined
>>> myval = None
>>> print(myval)
None
>>> myval = None
>>> if myval == None:
	print("The variable doesn't have a value")

	
The variable doesn't have a value
>>> if age == 10:
	print("What's the best way to speak to a monster?")
	print("From as far away as possible!")

	
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    if age == 10:
NameError: name 'age' is not defined
>>> age = 10
>>> age = '10'
>>> if age == 10:
	print("What's the best way to speak to a monster?")
	print("From as far away as possible!")

	
>>> 
>>> age = 10
>>> age = '10'
>>> converted_age = int(age)
>>> age = 10
>>> converted_age = str(age)
>>> age = '10'
>>> converted_age = int(age)
>>> if converted_age == 10:
	print("What's the best way to speak to a monster?")
	print("From as far away as possible!")

	
What's the best way to speak to a monster?
From as far away as possible!
>>> age = '10.5'
>>> converted_age = int(age)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    converted_age = int(age)
ValueError: invalid literal for int() with base 10: '10.5'
>>> age =
SyntaxError: invalid syntax
>>> ten
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    ten
NameError: name 'ten' is not defined
>>> age = 'ten'
>>> converted_age = int(age)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    converted_age = int(age)
ValueError: invalid literal for int() with base 10: 'ten'
>>> money = 2000
>>> if money > 1000:
	print("I'm rich!")
else:
	print("I'm not rich!!")
	  print("But I might be later...")
	  
SyntaxError: unexpected indent
>>> 
