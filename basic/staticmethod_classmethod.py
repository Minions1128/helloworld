# staticmethod vs. classmethod
class SC(object):
    flag = 1

    def fun(self):
        print 'this is basic function.'

    @staticmethod
    def static_fun():
        print 'this is static function.'
        print SC.flag
        SC().fun()

    @classmethod
    def class_fun(cls):
        print 'this is class function.'
        print cls.flag
        cls().fun()

    @classmethod
    def class_fun_2(_c):
        print 'this is class function 2.'
        print _c.flag
        _c().fun()


SC.static_fun()
print '@---------------------------------'
SC.class_fun()
print '#---------------------------------'
SC.class_fun_2()