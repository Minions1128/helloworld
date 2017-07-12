# -*- coding: UTF-8 -*-

##property()函数，有get，set，del以及日志四个参数，
##分别用于对象的查询、设置以及删除
class Number(object):
    def __init__(self, value):
        print "$$$ calling init"
        self.value = value
    def getNeg(self):
        print "$$$ calling get"
        return self.value
    def setNeg(self, value):
        print "$$$ calling set"
        self.value = -value
    def delNeg(self):
        print "$$$ calling del"
        del self.value
    _all = property(getNeg, setNeg, delNeg, "I'm negtive")


x = Number(1.1)
print "x._all = %s" % x._all
x._all = -22
print "x.value = %s" % x.value
print "Number._all.__doc__ is", Number._all.__doc__
del x._all


print '--------------------------------------------------------------------1'


# @property之后，将num定义为一个只读方法，不可修改其方法
class Number(object):
    def __init__(self, value):
        print "$$$ calling init"
        self.value = value
    def getNeg(self):
        print "$$$ calling get"
        return self.value

    @property
    def num(self):
        print "$$$ calling num"
        return self.value


x = Number(1.1)
print x.getNeg()
print x.num
x.getNeg = 1000
print x.getNeg
# x.num = 1 会报错
# print x.num


print '--------------------------------------------------------------------2'


# @property取代setter、getter和deleter方法
class Number(object):
    def __init__(self, value):
        print "$$$ calling init"
        self.value = value
    @property
    def num(self):
        print "$$$ calling num"
        return self.value
    @num.setter
    def num(self, value):
        self.value = value
        print "$$$ calling num.setter"
    @num.deleter
    def num(self):
        del self.value
        print "$$$ calling num.deleter"

x = Number(1.1)
print x.num
x.num = 99
print x.value
del x.num
