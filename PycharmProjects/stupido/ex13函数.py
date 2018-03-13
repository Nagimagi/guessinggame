#!/usr/bin/python
# -*- coding:utf-8 -*-


# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args # 参数解包的过程，可省略
    print "arg1 :%r, arg2: %r" % (arg1, arg2)


# Ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)


# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1


# this one takes one arguments
def print_none():
    print "I got nothin'."

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

# “‘运行函数(run)’、‘调用函数(call)’、和 ‘使用函数(use)’是同一个意思”





































