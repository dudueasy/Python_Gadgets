# -*- coding: utf-8 -*-
__author__ = 'apolo'
_date_ = '2018/1/23 上午8:19'

import socket
import shlex
import json

# import subprocess

# 创建socket对象
client_sk = socket.socket()

# 连接服务器, 参数为服务器的ip和端口.
address = ('127.0.0.1', 8001)

print('client 开始连接服务器')
client_sk.connect(address)

while True:

    command = input('请输入要执行的命令 : ')


    client_sk.sendall(command.encode())
    print('---信息已发送-->\n')

    # 服务器首先发送数据大小
    server_data =client_sk.recv(1024)
    data_size = int(server_data.decode())

    # 隔断两次接收
    client_sk.send('ok'.encode())
    # 初始化要接收的数据容器
    current_data = bytes()
    print('数据大小为 %i'%data_size)

    # 当已接收的数据大小等同于服务端的 data_size时, 跳出循环
    while len(current_data) != int(data_size):

        recv_data = client_sk.recv(1024)

        current_data += recv_data

    # 输出提示信息
    data = current_data.decode()
    print("来自服务器的数据\n%s" % data)

