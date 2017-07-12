# -*- coding: UTF-8 -*-
# modified in 15 MAR
# Class

class Bird(object):
    # 定义了一个类

    have_feather = True
    way_of_reproduction = 'egg'
    # 定义两个属性

    def move(self, dx, dy):
        # 定义一个方法
        position = [0, 0]
        position[0] = position[0] + dx
        position[1] = position[1] + dy
        return position

summer = Bird()
    # 声明一个对象

print summer.way_of_reproduction
print 'after move:', summer.move(5, 8)

print Bird.have_feather
Bird().move(6, 9)
    # 直接调用类中的属性和方法


# subClass

class Chicken(Bird):
    way_of_move = 'walk'
    possible_in_KFC = True

class Oriole(Bird):
    way_of_move = 'fly'
    possible_in_KFC = False

summer = Chicken()
print summer.have_feather
print summer.move(5, 8)


# 自我调用

class Human(object):

    laugh = 'hahahaha'

    def show_laugh(self):
        print self.laugh

    def laugh_10th(self):
        for i in range(10):
            self.show_laugh()

lilei = Human()
lilei.laugh_10th()


# __init__ 方法

class happyBird(Bird):
    def __init__(self, more_words):
        print "we are happy birds.", more_words

summer = happyBird('Happy, Happy!')

# __str__和__repr__
class test_str_repr(object):
    def __str__(self):
        return '__str__'

    def __repr__(self):
        return '__repr__'

my_bird = test_str_repr()

print '%r -- %r' % ('%r', my_bird)
print '%s -- %s' % ('%s', my_bird)


# 自定义list的方法

print [1, 2, 3] + [4, 5, 6]

class superList(list):
    def __sub__(self, b):
        a = self[:]
        b = b[:]
        while len(b)>0:
            element_b = b.pop()
            if element_b in a:
                a.remove(element_b)
        return a

print superList([1, 2, 3]) - superList([3, 4])
