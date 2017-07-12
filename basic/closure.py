# -*- coding: UTF-8 -*-

print "$$$$$$$$$$$1"
def line_conf():
	def line(x):
		return x**2
	return line 	#返回函数对象
my_line = line_conf()
print my_line(5)
#将函数看成一个对象，引用对象的方法
print line_conf()(4)

print "$$$$$$$$$$$2"
def line_conf(i):
	def line(x):
		return x**2
	print line(i)
line_conf(5)
#将外函数参数传递到内涵数

print "$$$$$$$$$$$3"
def line_conf():
	def line():
		return 2
	print line()
line_conf()
#内部函数直接返回函数返回值

print "$$$$$$$$$$$4"
def line_conf():
	def line():
		return 2
	return line()
print line_conf()
#内部函数返回值返回到外部函数返回值

print "$$$$$$$$$$$5"
def line_conf(a, b):
	def line(x):
		return a*x+b
	return line
print line_conf(1, 2)(5)
line1 = line_conf(1,1)
line2 = line_conf(4,5)
print line1(5), line2(5)
#综合测试
