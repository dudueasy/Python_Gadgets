#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint


def generate_random_str(random_length=8):
    str = ''
    for i in range(random_length):
        n = randint(1,62)
        if n < 11:
            # 返回数字
            str += chr(randint(48,57))

        elif n < 37:
            # 返回大写字母
            str += chr(randint(65,90))
        else:
            # 返回小写字母
            str += chr(randint(97,122))
    return str