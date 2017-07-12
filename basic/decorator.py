# -*- coding: UTF-8 -*-

"""
	0. traditional
	1. decorator,在一组函数中要执行相同的操作，可以使用
	2. decorator with parameter
	3. decorator class
	4. staticmethod和classmethod
"""

# 0. traditional
def square_sum1(a, b):
	# get sqare sum
	print "Input:", a, b
	return a**2 + b**2

def square_diff1(a, b):
	# get sqare diff
	print "Input:", a, b
	return a**2 - b**2

print "$$$ Triditional Version"
print square_sum1(3, 4)
print square_diff1(3, 4)

# 1. decorator
def decorator2(fun2):
	def new_F2(a, b):
		print "input", a, b
		return fun2(a, b)
	return new_F2

@decorator2
def square_sum2(a, b):
	return a**2 + b**2

@decorator2
def square_diff2(a, b):
	return a**2 - b**2

print "\n$$$ Decorator Version"
print square_sum2(3, 4)
print square_diff2(3, 4)

# 2. decorator with parameter
def pre_str(pre=''):
	# old decorator
	def decorator3(Fun):
		def new_F(a, b):
			print pre + "Input", a, b
			return Fun(a, b)
		return new_F
	return decorator3

# get square sum
@pre_str('^_^\n')
def square_sum3(a, b):
	return a**2 + b**2

# get square diff
@pre_str('T_T\n')
def square_diff3(a, b):
	return a**2 - b**2

print "\n$$$ Parameter Version:"
print square_sum3(3, 4)
print square_diff3(3, 4)

# 3. decorator class
def decorator_class(OldClass):
	class NewClass(object):
		def __init__(self, age):
			self.total_display = 0
			self.old = OldClass(age)
		def display(self):
			self.total_display += 1
			print "total display times is", self.total_display
			self.old.display()
	return NewClass

@decorator_class
class Bird(object):
	def __init__(self, age):
		self.age = age
	def display(self):
		print "my age is", self.age

print "\n$$$ Class Version:"
earLord = Bird(5)
for i in range(3):
	earLord.display()

# 4. classmethod & staticmethod
class A(object):
	bar = 1
	def foo(self):
		print 'foo'

	@staticmethod
	def static_foo():
		print 'static_foo'
		print A.bar
		A().foo()

	@classmethod
	def class_foo(_cls1):
		print 'class_foo'
		print _cls1.bar
		_cls1().foo()

A.static_foo()
A.class_foo()
"""
output:
	static_foo
	1
	foo
	class_foo
	1
	foo
"""
