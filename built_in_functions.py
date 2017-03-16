#-*- coding: UTF-8 -*-

print "binary:", 0b100
print "octonary:", 0o100
print "hexadecimal:", 0x100

"""
dir() help() len() len() open() range()
enumerate() zip() iter() map() filter() reduce()
"""

# type的用法1
print type(1)
#<type 'int'>
print type('a')
# <type 'str'>

# type用法2
class Father(object):
    a = 1
class Son1(Father):
    b = 2

Son2 = type('Son2', (Father,), dict(b=2))
# Son1和Son2的作用相同

# 数学运算
print "the absolute value of -5 is", abs(-5)
print "Round 2.5 is", round(2.5)
print "2**3 is", pow(2, 3)
print "2**3%5 is", pow(2, 3, 5)
print "is 2.3 bigger than 3.2?(yes -1, no 1)", cmp(2.3, 3.2)
print "9/2 and 9%2 are", divmod(9,2)
print "the max num is", max([1,5,2,9])
print "the min num is", min([9,2,-4,2])
print "the summary is", sum([2,-1,9,12])

# 类型转换
int("5")
float(2)
long("23")
str(2.3)
bool(0)
list((1,2,3))
tuple([2,3,4])

# 这些对象，相当于False：**, [], (), {}, 0, 0.0, '', **

print "the complex number 3-9i is", complex(3, -9)
print "corresponding value of letter \'A\' is", ord("A")
print "corresponding letter of 66 is", chr(66)
print unichr(65)                       # 数值65对应的unicode字符
print bin(56)                          # 返回一个字符串，表示56的二进制数
print hex(56)                          # 返回一个字符串，表示56的十六进制数
print oct(56)                          # 返回一个字符串，表示56的八进制数
print slice(5,2,-1)                    # 构建下标对象 slice
print dict(a=1,b="hello",c=[1,2,3])    # 构建词典 dictionary

##序列操作
all([True, 1, "hello!"])         # 是否所有的元素都相当于True值
any(["", 0, False, [], None])    # 是否有任意一个元素相当于True值
sorted([1,5,3])                  # 返回正序的序列，也就是[1,3,5]
reversed([1,5,3])                # 返回反序的序列，也就是[3,5,1]

class Student(object):
	def __init__(self, ID, Name, Sex):
		self.ID = ID
		self.Name = Name
		self.Sex = Sex
me = Student('101', 'shenzhejian', 'm')
print "If there is ID in object me?", hasattr(me, "ID")
print "If there is gender in object me?", hasattr(me, "gender")
print "me.Name is", getattr(me, "Name")
delattr(me, 'Name')		# 删除me中的Name属性
print "If object me produced by class Student?", isinstance(me, Student)
print "If Student is sub-class of object?", issubclass(Student, object)

# Input
print raw_input("Please input string:")

print input("Please input a number")

import getpass
print getpass.getpass('password:')
