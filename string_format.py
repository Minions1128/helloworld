#-*- coding: UTF-8 -*-

# 3 kinds methods output string

str_a = "I'm %s, and %d year old"
para_a = ('Vamei', 99)
print str_a % para_a

str_b = "I'm %(name)s, and %(age)d year old"
para_b = {'name':'Vamei', 'age':99}
print str_b % para_b

print "I'm {name}, and {age} year old".format(name='Vamei', age=99)
# str_c = "I'm {name}, and {age} year old"
# para_c = {'name':'Vamei', 'age':99}
# print str_c.format(**para_c)


"""
%[(name)][flags][width].[precision]typecode
(name)为命名
flags可以有+,-,' '或0。+表示右对齐。-表示左对齐。' '为一个空格，
    表示在正数的左侧填充一个空格，从而与负数对齐。0表示使用0填充。
width表示显示宽度
precision表示小数点后精度
typecode见下表

%s    字符串 (采用str()的显示)
%r    字符串 (采用repr()的显示)
%c    单个字符
%b    二进制整数
%d    十进制整数
%i    十进制整数
%o    八进制整数
%x    十六进制整数
%e    指数 (基底写为e)
%E    指数 (基底写为E)
%f    浮点数
%F    浮点数，与上相同
%g    指数(e)或浮点数 (根据显示长度)
%G    指数(E)或浮点数 (根据显示长度)
%%    字符"%"
"""
print("%+10x" % 10)
print("%04d" % 5)
print("%06.3f" % 2.3)
print("%.*f" % (4, 1.2)) 
