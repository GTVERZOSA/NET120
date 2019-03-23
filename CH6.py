Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 23 2018, 23:31:17) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("hello")
hello
>>> print("hello")
hello
>>> print("hello")
hello
>>> print("hello
	  
SyntaxError: EOL while scanning string literal
>>> print("hello")
	  
hello
>>> print("hello")
	  
hello
>>> for x in range(0,5):
	  print('hello')

	  
hello
hello
hello
hello
hello
>>> print(list(range(10,20)))
	  
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> for x in range(0, 5):
	  print('hello %s; % x)
		
SyntaxError: EOL while scanning string literal
>>> for x in range(0, 5):
		print('hello %s' % x)

		
hello 0
hello 1
hello 2
hello 3
hello 4
>>> 
		
>>> wizard_list = ['spder legs', 'toe of frog', 'snail tongue'. 'bat wing', 'slug butter', 'bear burp']
		
SyntaxError: invalid syntax
>>> wizard_list = ['spder legs', 'toe of frog', 'snail tongue', 'bat wing', 'slug butter', 'bear burp']
		
>>> for i in wizard_list:
		print(i)

		
spder legs
toe of frog
snail tongue
bat wing
slug butter
bear burp
>>> wizard_list = ['spider legs', 'toe of frog', 'snail tongue', 'bat wing', 'slug butter', 'bear burp']
		
>>> print(wizard_list[0])
		
spider legs
>>> print(wizard_list[1])
		
toe of frog
>>> print(wizard_list[2])
		
snail tongue
>>> print(wizard_list[3])
		
bat wing
>>> print(wizard_list[4])
		
slug butter
>>> print(wizard_list[5])
		
bear burp
>>> 
		
>>> hugehairypants = ['huge', 'hairy', 'pants']
		
>>> for i in hugehairypants:
		print(i)
		print(i)

		
huge
huge
hairy
hairy
pants
pants
>>> 
		
>>> 
		
>>> hugehairypants = ['huge', 'hairy', 'pants']
		
>>> for i in hugehairypants:
		print(i)
		for j in hugehairypants:
			print(j)

		
huge
huge
hairy
pants
hairy
huge
hairy
pants
pants
huge
hairy
pants
>>> 
		
>>> 20 + 10 * 365 - 3 * 52
		
3514
>>> 
		
>>> found_cois = 20
		
>>> found_coins = 20
		
>>> magic_coins = 70
		
>>> stolen_coins = 3
		
>>> coins = found_coins
		
>>> for week in range(1, 53):
	coins = coins + magic_coins - stolen_coins
	print ('Week %s = %s' % (week, coins))

		
Week 1 = 87
Week 2 = 154
Week 3 = 221
Week 4 = 288
Week 5 = 355
Week 6 = 422
Week 7 = 489
Week 8 = 556
Week 9 = 623
Week 10 = 690
Week 11 = 757
Week 12 = 824
Week 13 = 891
Week 14 = 958
Week 15 = 1025
Week 16 = 1092
Week 17 = 1159
Week 18 = 1226
Week 19 = 1293
Week 20 = 1360
Week 21 = 1427
Week 22 = 1494
Week 23 = 1561
Week 24 = 1628
Week 25 = 1695
Week 26 = 1762
Week 27 = 1829
Week 28 = 1896
Week 29 = 1963
Week 30 = 2030
Week 31 = 2097
Week 32 = 2164
Week 33 = 2231
Week 34 = 2298
Week 35 = 2365
Week 36 = 2432
Week 37 = 2499
Week 38 = 2566
Week 39 = 2633
Week 40 = 2700
Week 41 = 2767
Week 42 = 2834
Week 43 = 2901
Week 44 = 2968
Week 45 = 3035
Week 46 = 3102
Week 47 = 3169
Week 48 = 3236
Week 49 = 3303
Week 50 = 3370
Week 51 = 3437
Week 52 = 3504
>>> 
