Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 23 2018, 23:31:17) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list(range(0,5))
[0, 1, 2, 3, 4]
>>> list (range(0, 1000))

>>> def testfunc(Gerald):
	print('hello %s' % myname)

	
>>> testfunc('Mary')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    testfunc('Mary')
  File "<pyshell#4>", line 2, in testfunc
    print('hello %s' % myname)
NameError: name 'myname' is not defined
>>> testfunc('Mary')
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    testfunc('Mary')
  File "<pyshell#4>", line 2, in testfunc
    print('hello %s' % myname)
NameError: name 'myname' is not defined
>>> def testfunc(myname):
	print(hello %s' % myname)
	      
SyntaxError: EOL while scanning string literal
>>> def testfunc(myname):
	      print('hello %s' % myname)

	      
>>> testfunc('Mary')
	      
hello Mary
>>> def testfunc(fname, lname):
	      print('Hello %s %s' % (fname, lname))

	      
>>> testfunc('Mary', 'Smith')
	      
Hello Mary Smith
>>> 
	      
>>> firstname = 'Joe'
	      
>>> lastname = 'Robertson'
	      
>>> testfunc(firstname, lastname)
	      
Hello Joe Robertson
>>> 
	      
>>> def savings(pocket_money, paper_route, spending):
	      return pocket_money + paper_route - spending

	      
>>> print(savings(10, 10, 5))
	      
15
>>> def variable_test():
	first_variable = 10
	second_variable = 20
	return first_variable * second_variable

	      
>>> print(variable_test())
	      
200
>>> print(first_variable)
	      
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    print(first_variable)
NameError: name 'first_variable' is not defined
>>> another_variable = 100
	      
>>> def variable_test2():
	first_variable = 10
	second_variable = 20
	return first_variable * second_variable * another_variable

	      
>>> print(variable_test2())
	      
20000
>>> def spaceship_building(cans):
	total_cans = 0
	for week in range(1, 53):
		total_cans = total_cans + cans
		print('Week %s = %s cans' % (week, total_cans))

	      
>>> spaceship_buildings(2)
	      
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    spaceship_buildings(2)
NameError: name 'spaceship_buildings' is not defined
>>> spaceship_building(2)
	      
Week 1 = 2 cans
Week 2 = 4 cans
Week 3 = 6 cans
Week 4 = 8 cans
Week 5 = 10 cans
Week 6 = 12 cans
Week 7 = 14 cans
Week 8 = 16 cans
Week 9 = 18 cans
Week 10 = 20 cans
Week 11 = 22 cans
Week 12 = 24 cans
Week 13 = 26 cans
Week 14 = 28 cans
Week 15 = 30 cans
Week 16 = 32 cans
Week 17 = 34 cans
Week 18 = 36 cans
Week 19 = 38 cans
Week 20 = 40 cans
Week 21 = 42 cans
Week 22 = 44 cans
Week 23 = 46 cans
Week 24 = 48 cans
Week 25 = 50 cans
Week 26 = 52 cans
Week 27 = 54 cans
Week 28 = 56 cans
Week 29 = 58 cans
Week 30 = 60 cans
Week 31 = 62 cans
Week 32 = 64 cans
Week 33 = 66 cans
Week 34 = 68 cans
Week 35 = 70 cans
Week 36 = 72 cans
Week 37 = 74 cans
Week 38 = 76 cans
Week 39 = 78 cans
Week 40 = 80 cans
Week 41 = 82 cans
Week 42 = 84 cans
Week 43 = 86 cans
Week 44 = 88 cans
Week 45 = 90 cans
Week 46 = 92 cans
Week 47 = 94 cans
Week 48 = 96 cans
Week 49 = 98 cans
Week 50 = 100 cans
Week 51 = 102 cans
Week 52 = 104 cans
>>> spaceship_building(13)
	      
Week 1 = 13 cans
Week 2 = 26 cans
Week 3 = 39 cans
Week 4 = 52 cans
Week 5 = 65 cans
Week 6 = 78 cans
Week 7 = 91 cans
Week 8 = 104 cans
Week 9 = 117 cans
Week 10 = 130 cans
Week 11 = 143 cans
Week 12 = 156 cans
Week 13 = 169 cans
Week 14 = 182 cans
Week 15 = 195 cans
Week 16 = 208 cans
Week 17 = 221 cans
Week 18 = 234 cans
Week 19 = 247 cans
Week 20 = 260 cans
Week 21 = 273 cans
Week 22 = 286 cans
Week 23 = 299 cans
Week 24 = 312 cans
Week 25 = 325 cans
Week 26 = 338 cans
Week 27 = 351 cans
Week 28 = 364 cans
Week 29 = 377 cans
Week 30 = 390 cans
Week 31 = 403 cans
Week 32 = 416 cans
Week 33 = 429 cans
Week 34 = 442 cans
Week 35 = 455 cans
Week 36 = 468 cans
Week 37 = 481 cans
Week 38 = 494 cans
Week 39 = 507 cans
Week 40 = 520 cans
Week 41 = 533 cans
Week 42 = 546 cans
Week 43 = 559 cans
Week 44 = 572 cans
Week 45 = 585 cans
Week 46 = 598 cans
Week 47 = 611 cans
Week 48 = 624 cans
Week 49 = 637 cans
Week 50 = 650 cans
Week 51 = 663 cans
Week 52 = 676 cans
>>> 
