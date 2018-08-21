#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re

# 获取文件大小的工具函数


def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def file_size(file_path):
    """
    this function will return the file size
    """
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return convert_bytes(file_info.st_size)


print('欢迎使用apolo的文件小助手')

# 开启循环
while True:
    # 获取工作目录
    user_input = input("请输入工作目录的绝对路径:\n")
    print(user_input)

    if not os.path.isdir(user_input):
        print('路径无效, 请输入正确的路径')
        continue

    elif not user_input == 'q' and os.path.isdir(user_input):
        print('工作目录有效, 正在生成文件信息')
        working_directory = user_input

        directory_info = os.path.join(working_directory, 'files_info.txt')

        # 遍历目录生成文件信息
        with open(directory_info, 'w') as fileobj:
            try:
                g = os.walk(working_directory)
                for i in g:
                    # print(i)
                    for j in i[-1]:
                        # 获取绝对路径
                        file_abs_path = os.path.join(i[0], j)

                        # 获取相对路径
                        file_path = file_abs_path.replace(working_directory,'')

                        current_info = "路径: {0}  文件大小: {1} \n".format(
                            file_path, file_size(file_abs_path))
                        # print(j)
                        if 'files_info' in file_path or '.DS_Store' in file_path:
                            continue
                        fileobj.write(current_info)

            except StopIteration:
                print('工作完成')
                exit(0)
