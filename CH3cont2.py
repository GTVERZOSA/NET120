Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 23 2018, 23:31:17) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list1 = [1, 2, 3, 4]
>>> list2 = ['I', 'tripped', 'over', 'and', 'hit', 'the', 'floor']
>>> print(list1+list2)
[1, 2, 3, 4, 'I', 'tripped', 'over', 'and', 'hit', 'the', 'floor']
>>> list1 = [1, 2, 3, 4]
>>> list2 = ['I', 'ate', 'chocolate', 'and', 'I', 'want', 'more']
>>> list3 = list1 + list2
>>> print(list3)
[1, 2, 3, 4, 'I', 'ate', 'chocolate', 'and', 'I', 'want', 'more']
>>> list1 = [1, 2]
>>> print(list1*5)
[1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
>>> 
>>> list1 / 20
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    list1 / 20
TypeError: unsupported operand type(s) for /: 'list' and 'int'
>>> list1 - 20
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    list1 - 20
TypeError: unsupported operand type(s) for -: 'list' and 'int'
>>> list1 + 50
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    list1 + 50
TypeError: can only concatenate list (not "int") to list
>>> 
>>> fibs = (0, 1, 2, 2, 3)
>>> print(fibs[3])
2
>>> fibs[0] = 4
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    fibs[0] = 4
TypeError: 'tuple' object does not support item assignment
>>> 
