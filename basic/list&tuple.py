# -*- coding: UTF-8 -*-
"""
	介绍list和tuple的基础特性，以及list的一些输出形式和方法
"""

s1 = (2, 1.3, 'love', False)
	# 定义一个tuple

s2 = [12, 12.3, 'smile', True]
	# 定义一个list

s3 = [1,[3,4,5.6]]
s33 = [s1,s2]
	# 定义嵌套list

# tuple一旦被创建之后，无法更改其中元素，而list可以

print "s1[0] = ", s1[0]
	# 输出s1中的第一个元素

s2[1] = 'shen'
	# 修改s2中的第一个元素

print "s3[1][2] = ", s3[1][2]
	# 输出嵌套list中的元素

# list的其他形式的输出
s2 = [1,2,3,4,5,1.3,2]
print s2[:5]		  	  # 从开始到下标4（下标5的元素 不包括在内）
print s2[2:]		  	  # 从下标2到最后
print s2[0:5:2]		  	# 从下标0到下标4 (下标5不包括在内)，每隔2取一个元素 （下标为0，2，4的元素）
print s2[2:0:-1]	  	# 从下标2到下标1
print s2[-3]			    # 序列倒数第三个元素
print s2.count(2)		  # 计数，看总共有多少个5
print s2.index(1.3)		# 查询s2的第一个1.3的下标
print s2.pop()	  		# 从s2中去除最后一个元素，并将该元素返回。
print "the length of the list is", len(s2)
print "the min element is", min(s2)
print "the max element is", max(s2)
print "if all the element is True?", all(s2)
print "is any element is True?", any(s2)
print "the summary of the element is", sum(s2)

# list的一些方法
s2.append(6)		  	# 在s2的最后增添一个新元素6
s2.sort()			    	# 对s2的元素排序
s2.remove(2)		  	# 从s2中去除第一个2
s2.insert(0,9)			# 在下标为0的位置插入9
s2.extend(s)			# 将整个s加在s2后面
s2.reverse()			# 将s2逆置
del s2[1]			# 将s2的下标为1的元素删除

# List comprehension
L1 = []
L1 = [x**2 for x in range(10)]
"""
等价于
for x in range(10):
	L1.append(x**2)
"""

x1 = [1,3,5]
y1 = [9,12,13]
L = [ x**2 for (x,y) in zip(x1,y1) if y>10 ]
print L
"""
等价于
for (x, y) in zip(x1, y1):
	if y > 10:
		L.append(x**2)
"""
