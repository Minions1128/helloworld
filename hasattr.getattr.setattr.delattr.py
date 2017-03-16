class Cls_A(object):
    def __init__(self):
        self.name = 'zhejian'
        # self.age = 26

    # def method(self):
    #     print 'method print'


def not_find_method():
    print 'not find method in function.'


obj_a = Cls_A()


print hasattr(obj_a, 'name')
print hasattr(obj_a, 'age')
# print if there is 'age' attribute in obj_a


print getattr(obj_a, 'name', 'not find name')
# If there 'name' attribute in obj_a, print it, 
# else print 'not find name'
print getattr(obj_a, 'age', 'not find age')
print getattr(Cls_A, 'method', 'not find method')
# If there 'method' method in obj_a, print it,
# else print 'not find method'.
getattr(obj_a, 'method', not_find_method)()


setattr(obj_a, 'name', 'haha')
# It will change or add the value of 'name' attribute.
print obj_a.name


delattr(obj_a, 'name')
# delete attribute of obj_a, which belongs obj_a. 
print dir(obj_a)
