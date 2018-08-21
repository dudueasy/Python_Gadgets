#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import os, re

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
        print('工作目录有效')
        working_directory = user_input
        # 获取处理的文件类型

        while True:
            file_type = input("请输入要移动的文件类型(支持文件名, 后缀名和正则表达式):\n")
            confirm = input("确认处理 {0} 类型文件? y/n\n".format(file_type))

            if confirm != 'y':
                continue

            while True:
                target_directory = input("请输入目标路径:\n")
                if not os.path.isdir(target_directory):
                    print("路径无效")
                    continue
                else:
                    print('{0} 路径可用'.format(target_directory))
                    print('开始移动文件')

                    # 遍历目录移动文件
                    try:
                        files = os.walk(working_directory)

                        while True:
                            output = next(files)
                            for file in output[2]:
                                filepath = os.path.join(output[0], file)
                                if os.path.isfile(filepath) and re.search(file_type.lower(), file.lower()):
                                    os.rename(filepath, os.path.join(target_directory, file))
                    except StopIteration:
                        print('工作完成')
                        exit(0)
