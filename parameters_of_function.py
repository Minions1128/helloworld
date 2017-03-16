# -*- coding: UTF-8 -*-

"""
	介绍了函数参数的传递过程：
	1，list参数传递
	2，参数的打包
	3，开包
	4，函数作为参数
"""

# 参数传递
a = 1
def plus(a):
        a += 1
        return a
print plus(a)
print a
"""
	输出结果：2,1
"""
b = [1, 2, 3]
def pluss(b):
        b[0] += 1
        return b
print pluss(b)
print b
"""
	输出结果：
	[2, 2, 3]
	[2, 2, 3]
"""

# 参数的默认值
def f(a, b, c):
	# 未使用默认参数
    return a + b + c
print f(1, 2, 3)

def fun1(a, b, c=3):
	# 有默认值的参数只能放在多个函数参数的后面
    return a + b + c
print fun1(2, 3)
	# 2, 3分别为a和b的值，c的值为默认值

print fun1(c=1, a=2, b=3)
	# 可以将参数的位置进行调换，但其名称无法改变

# 参数打包
def func(*nameshen):
    # 参数相当于tuple
    print nameshen
func(1,4,6)
func(5,6,7,1,2,3)

def func(**dictzhe):
    # 参数相当于dict
    print dictzhe
func(a=1,b=9)
func(m=2,n=1,c=11)

print "\nUnpacking"
def func(a,b,c):
    print a,b,c

args = (1,3,4)
func(*args)     #tuple的数量必须和函数的数量相同

dictJian = {'a':1,'b':2,'c':3}
func(**dictJian)    #dict中的key和value必须与func中的一致


print "\nfunction as arguements"
def func(x,y):
    return x+y
def test(f,a,b):
    print 'test'
    print f(a,b)
test(func, 3, 5)
test((lambda x, y:x**2+y), 6, 9)
