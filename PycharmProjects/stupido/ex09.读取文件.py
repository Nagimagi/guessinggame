#!/usr/bin/python
# -*- coding:utf-8 -*-
# 导入参数变量argv（argument variable）
from sys import argv

# 将argv解包（unpack），将所有的参数一次赋予左边的变量名
script, filename = argv

# 打开文件
txt = open(filename)

# 打开filename指定的文件名，并打印出读取的内容
print "Here's your file %r:" % filename
print txt.read()

# 不用变量filename，手动输入文件名
# print "Type the filename again: "
# file_again = raw_input(">> ")
#
# # 打开刚才手动输入文件名的文件
# txt_again = open(file_again)
#
# # 打印出文件内容
# print txt_again.read()












