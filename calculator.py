""" the basic calculator"""
i = input('what do you want to calculate: ')
i = list(i)
"""the calculator function"""
def calculate(a):
		
	#the add function
	def add(b, c):
		d = b + c
		return d
	# the subtract function
	def minus(b, c):
		d = b - c
		return d
	#the multiply function
	def multiply(b, c):
		d = b * c
		return d
	#the divide function
	def divide(b, c):
		d = b / c
		return d
		
		"""using the global i"""
	global i
	
	"""performing the calculations on the numbers"""
	for k in i:
		if i == '+' or i == '-' or i == '/' or i == '*':
			
			num1 = int(''.join(i[:k-1]))
	    	num2 = int(''.join(i[k+1:]))
	        
		if i == '+':
	    	add(num1, num2)
		elif i == '-':
			minus(num1, num2)
		elif i == '*':
			multiply(num1, num2)
		elif i == '/':
			divide(num1, num2)
		else:
			print('input the right operator')
			
	return a
	
calculator(i)
	
