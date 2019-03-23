Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 23 2018, 23:31:17) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import time
>>> print(time.asctime())
Fri Mar 22 16:52:30 2019
>>> print (time.asctime())
Fri Mar 22 16:52:44 2019
>>> print (time.asctime())
Fri Mar 22 16:52:56 2019
>>> print (time.asctime())
Fri Mar 22 16:53:03 2019
>>> print (time.asctime())
Fri Mar 22 16:53:12 2019
>>> 
>>> import sys
>>> print(sys.stdin.readline())



>>> if age >= 10 and age <= 13:
	print('What is 13 + 49 + 84 + 155 + 97? A headache!')
else:
	print('Huh'?)
	
SyntaxError: invalid syntax
>>> if age >= 10 and age <= 13:
	print('What is 13 + 49 + 84 + 155 + 97? A headache!')
else:
	print('Huh?')

	
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    if age >= 10 and age <= 13:
NameError: name 'age' is not defined
>>> def silly_age_joke(age):
	if age >= 10 and ange <= 13:
		print('What is 13 + 49 + 84 + 155 + 97? A headache!')
	else:
		print('Huh?')

		
>>> silly_age_joke(9)
Huh?
>>> silly_age_joke(10)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    silly_age_joke(10)
  File "<pyshell#19>", line 2, in silly_age_joke
    if age >= 10 and ange <= 13:
NameError: name 'ange' is not defined
>>> silly_age_joke(10)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    silly_age_joke(10)
  File "<pyshell#19>", line 2, in silly_age_joke
    if age >= 10 and ange <= 13:
NameError: name 'ange' is not defined
>>> NameError: name 'ange' is not defined
SyntaxError: invalid syntax
>>> def silly_age_joke(age):
	if age >= 10 and age <= 13:
		print('What is 13 + 49 + 84 + 155 + 97? A headache!')
	else:
		print('Huh?')

		
>>> silly_age_joke(10)
What is 13 + 49 + 84 + 155 + 97? A headache!
>>> 
>>> def silly_age_joke():
	print('How old are you?')
	age = int(sys.stdin.readline())
	if age >= 10 and age <= 13:
		print('What is 13 + 49 + 84 + 155 + 97? A headache!')
	else:
		print('Huh?')

		
>>> silly_age_joke()
How old are you?
10
What is 13 + 49 + 84 + 155 + 97? A headache!
>>> silly_age_joke()
How old are you?
15
Huh?
>>> def are_you_hungry():
	print('Are you hungry?')
	answer = (int(sys.stdin.readline())
	if answer < yes and answer < no:
		  
SyntaxError: invalid syntax
>>> def are_you_hungry():
	print('Are you hungry?')
	answer = (int(sys.stdin.readline())
	if answer = yes and answer = no:
		  
SyntaxError: invalid syntax
>>> def are_you_hungry():
	print('Are you hungry?')
	answer = (int(sys.stdin.readline())
	if answer >= yes and answer <= no:
		  
SyntaxError: invalid syntax
>>> are_you_hungry
		  
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    are_you_hungry
NameError: name 'are_you_hungry' is not defined
>>> are_you_hungry()
		  
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    are_you_hungry()
NameError: name 'are_you_hungry' is not defined
>>> def are_you_hungry():
	print('Are you hungry?')

		  
>>> are_you_hungry()
		  
Are you hungry?
>>> yes
		  
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    yes
NameError: name 'yes' is not defined
>>> 
