#-*- coding: UTF-8 -*-
str1 = 'abcdefghijk'
print "str1 =", str1
print "str1[1] =", str1[1]
print "str1[2:6:2] =", str1[2:6:2]

# for i in range(0,len(str1),2):
#     print str1[i]

for (index, char) in enumerate(str1):
	print "str1[%s] = %s" % (index, char)


str2 = "s1234subway, SUBway, Subway, sUBway, subway"
print "the string str2 is$$$", str2
print "the frequency of \"sub\" occurrences is", str2.count("sub")
print "the first time \"sub\" appread is index of",str2.find("sub")
"""
find()函数找不到后返回-1；
index()函数，其若找不到，则举出错误；
还有rfind()和rindex()函数，其查找方式从右边开始
"""
print "if the list is all num or letter?", str2.isalnum()
print "if the list is all letter?", str2.isalpha()
print "if the list is all num?", str2.isdigit()
print "if the letter is init upper case?", str2.istitle()
print "if the list is all space?", str2.isspace()
print "if the list is all low case?", str2.islower()
print "if the list is all up case?", str2.isupper()
print "split:\n", str2.split()
"""
str.split([sep, [max]])函数，其功能为将str字符串按照sep进行分割，最发分割max次，
参数如果参数均为空，则表示将str按照空格进行分割尽可能多的次数
max为空则表示按照sep分割尽可能多的次数
与其类似的还有str.rsplit([sep,[max]])函数，其是按照从右向左进行查找和分割
"""
print "\nstr2 as the split sign to connect args:\n", str2.join("&&&&")
print "\nremove the \"way\" in front and rear of the string:\n", str2.strip("way")
print "\nrelpace \"way\" to \"$$$\"\n", str2.replace("way", "$$$")
print "\nInit Upper case:\n", str2.capitalize()
print "\nall lower case:\n", str2.lower()
print "\nall upper case:\n", str2.upper()
print "\nswap upper and lower case:\n", str2.swapcase()
print "\nall letter init upper case:\n", str2.title()
print "\ntotal length 300, str2 in the center:\n", str2.center(300)
print "\ntotal length 300, str2 in the left:\n", str2.ljust(300)
print "\ntotal length 300, str2 in the right:\n", str2.rjust(300)
