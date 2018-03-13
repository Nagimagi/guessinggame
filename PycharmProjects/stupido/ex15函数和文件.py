#!/usr/bin/python
# -*- coding:utf-8 -*-
from sys import argv

script, input_file = argv


def print_all(f):
    print f.read()


def rewind(f):
    f.seek(7, 0)        # 设置读取指针
# seek(offset, whence = 0),
# offset:开始的偏移量，也就是代表需要移动偏移的字节数，
# whence：给offset参数一个定义，表示要从哪个位置开始偏移；
# 0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起


def print_a_line(line_count, f):
    print line_count, f.readline()  # 第几行，读取内容


current_file = open(input_file)     # 打开输入的文件名

print "First let's print the whole file:\n"

print_all(current_file)     # 打印文件所有内容

print "Now let's rewind, kind of like a tape."

rewind(current_file)        # 调用读取指针，可通过调用的位置调整读取指针

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)





































