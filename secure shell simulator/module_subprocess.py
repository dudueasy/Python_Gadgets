# -*- coding: utf-8 -*-
__author__ = 'apolo'
_date_ = '2018/1/23 上午8:28'


# 通过 subprocess对象获得命令输出的两种方法:
# 方法1

# 必须定义 stdout = PIPE 才能获得子进程的标准输出.
# PIPE对象是一个file_obj对象. 调用 read() 来获取值
# a = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
# print(a.stdout.read().decode())


# 方法2
# 直接使用 subprocess.check_output() 方法
# output = subprocess.check_output(command).decode()
# print(output)
