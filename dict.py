# -*- coding: UTF-8 -*-

'''
字典相关
'''

dict1 = { 'Tom':89, 'Sam':57 , 'Lily':100}
# 定义一个字典

print dict1['Tom']
# 输出某个key所对应的value

dict1['Sam'] = 60
# 修改某个key所对应的value

dict1['Jesse'] = 149
# 添加一项

for k in dict1:
	# 遍历字典中的value、
	print k, dict1[k]

print 'output all keys in the dict with list pattern', dict1.keys()
print 'output all values in the dict with list pattern', dict1.values()
print 'output all the pairs of key and value in the dict with list pattern', dict1.items(), type(dict1.items())
print 'each pairs of key and value is tuple', dict1.items()[3], type(dict1.items()[3])

print 'the length of dict is', len(dict1)
del dict1['Tom']
# 删除字典中key为Tom的项

dict1.clear()
# 清空字典


def dict_para(**params):
	# 利用字典传递参数
	print params
	a = params.pop('a', 0)
	b = params.setdefault('b', 0)
	c = params.get('c', 0)
	# 这三种方法的区别是，pop会删除原来项，setdefault会添加项，而get不会造成任何影响
	print "a = %s, b = %s, c = %s" % (a, b, c)

dict_para(c=1, a=2, d=3)
