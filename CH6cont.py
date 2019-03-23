Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 23 2018, 23:31:17) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for step in range (0, 20):
	print(step)
step = 0
SyntaxError: invalid syntax
>>> for step in range (0, 20):
	print(step)
	step = 0
	whilte step < 10000:
		
SyntaxError: invalid syntax
>>> for step in range (0,20):
	print(step)
	step = 0
	while step < 10000:
		print(step)
		if tired == True:
			break
		elif badweather == True:
			break
		else:
			step = step+1

			
0
0
Traceback (most recent call last):
  File "<pyshell#18>", line 6, in <module>
    if tired == True:
NameError: name 'tired' is not defined
>>> x = 45
>>> y = 80
>>> while x < 50 and y < 100:
	x = x + 1
	y = y + 1
	print(x, y)

	
46 81
47 82
48 83
49 84
50 85
>>> 
>>> while True:
	lots of code here
	
SyntaxError: invalid syntax
>>> while True:
	"Lost of code here"
	"Lots of code here"
	"Lots of code here"
	if some_value == True:
		break

	
'Lost of code here'
'Lots of code here'
'Lots of code here'
Traceback (most recent call last):
  File "<pyshell#36>", line 5, in <module>
    if some_value == True:
NameError: name 'some_value' is not defined
>>> 
