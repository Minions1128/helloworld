# -*- coding: UTF-8 -*-

"""
	1. class.__dict__，查询class中的属性
	2. class.__call__()，调用时执行次函数
	3. class.__getattr__(self, name)，查询对象的属性
	   class.__setattr__()，给属性赋值
"""

# 1. class.__dict__
class Bird(object):
    feature = True

class Chicken(Bird):
    fly = False
    def __init__(self, age):
        self.age = age

summer = Chicken(2)
print "summer.age IS %s" % summer.age

print "Bird.__dict__ IS %s" % Bird.__dict__
print "Chicken.__dict__ IS %s" % Chicken.__dict__
print "summer.__dict__ IS %s" % summer.__dict__

summer.__dict__['age'] = 3
print "summer.__dict__['age'] IS %s" % summer.__dict__['age']
print "summer.age IS %s" % summer.age
summer.age = 5
print "summer.__dict__['age'] IS %s" % summer.__dict__['age']


# 2. class.__call__()
class SampleMore(object):
	def __call__(self, a):
		print "$$$ calling call"
		return a**5

add = SampleMore()
print "add(2) = %s" % add(2)


# 3. class.__getattr__(), class.__setattr__()
class Human(object):
	def __init__(self, age):
		self.age = age
	def __getattr__(self, name):
		if name == 'adult':
			if self.age >= 18:
				return True
			else:
				return False
		else:
			print 'THERE IS NO ATTR', name
	def __setattr__(self, name, value):
		self.__dict__[name] = value

	def __delattr__(self, name):
		del self.__dict__[name]


Tom = Human(18)
print 'Tom is adult?', Tom.adult
Tom.age = 17
print 'Tom is adult?', Tom.adult
Tom.male = 3
print Tom.male
