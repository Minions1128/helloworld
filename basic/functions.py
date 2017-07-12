# -*- coding: UTF-8 -*-
"""
  1. zip
  2. lambda
  3. map()
  4. filter()
  5. generator
"""

"""
  zip
"""
a = [1, 2, 3, 4]
b = [1.1, 2.1, 3.1, 4.1]
c = ['a', 'b', 'c', 'd']

abc = zip(a, b, c)
# ta, tb, tc, td = zip(a, b, c)

print "zip(a, b, s) = %s" % abc
print "the type of abc is %s" % type(abc)
print "the type of abc[1] is %s" % type(abc[1])

"""
  unzip
"""
unzip_abc = zip(*abc)
# na, nb, nc = zip(ta, tb, tc, td)


"""
  lambda
"""
func = lambda x,y: x+y
# Equivalent to:
# def func(x,y):
#     return x+y


"""
  map()函数，将函数对象以次作用于表的每一个元素
"""
print map((lambda x:x**2),[1,2,3,4])
#[1, 4, 9, 16]
print map((lambda x,y:x+y),[1,2,3],[6,7,9])
#[7, 9, 12]

"""
  filter()
"""
def func(a):
  if a > 100:
    return True
  else:
    return False
print filter(func, [10, 56, 101, 500])

"""
  reduce()函数，累计地将函数作用于各个参数
"""
print reduce((lambda x,y:x+y),[1,2,3,4,5])
"""
等价于：
print (((1+2)+3)+4)+5
"""

"""
  generator
"""
def gen():
    a = 100
    yield a
    a = a * 8
    yield a
    yield 1000

for i in gen():
    print i

def gen1():
    for i in range(4):
        yield i
for i in gen1():
    print i

#gen2可以写为等价于gen1的形式
gen2 = (x for x in range(4))
for i in gen2:
    print i
