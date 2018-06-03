#!/usr/bin/env python
# encoding: utf-8
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: LogDecorator.py
@time: 18-6-3 下午4:07
@version: v1.0 
"""


def PrintfDecorator(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)

        print("{function}({args}) ----> {result}\n".format(function=func.__name__,
                                                           args=", ".join(str(i) for i in args),
                                                           result=res))
        return res

    return wrapper
