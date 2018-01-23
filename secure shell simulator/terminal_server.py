# -*- coding: utf-8 -*-
__author__ = 'apolo'
_date_ = '2018/1/23 上午8:18'

import socket
import subprocess
import json
import shlex
import traceback

# 创建一个socket对象
server_sk = socket.socket()
# 创建ip地址和端口
address = ('127.0.0.1', 8002)
# 绑定ip地址和端口
server_sk.bind(address)
# 开始监听, 参数中设置允许排队的连接数, 超出的连接会被服务器拒绝
server_sk.listen(3)

# 自定义一个 bytes 转换器
def get_bytes(n):
    return str(n).encode()

while True:
    # 等待客户端请求, 接受到请求的时候会获得一个元组. 获取元组的第一个对象作为连接对象
    print('server开始等待客户端连接请求\n')
    conn, addr = server_sk.accept()
    print('已经和客户端 {0} 建立连接'.format(addr))

    # 开始持续通信
    while True:
        try:
            data = conn.recv(1024)

            # 如果没有数据那就直接出本次持续通信, 等待建立新的连接
            if not data: break

            # 将 bytes 转换成unicode , 然后分解为列表
            data = data.decode()
            data = shlex.split(data)

            print("message from remote: %s\n" % data)

            # 错误处理
            try:
                msg = subprocess.check_output(data, shell=True)

                # popen_obj = subprocess.Popen(data, shell=True,stdout=subprocess.PIPE)
                # msg = popen_obj.stdout.read()

            except Exception as e:
                # convert Exception object firstly to string, then bytes
                msg = get_bytes(e)

            # 先发送数据的长度给客户端

            data_size = get_bytes(len(msg))
            print('数据大小: %s' % str(data_size))

            conn.sendall(data_size)
            conn.sendall(msg)
            print('---命令输出已返回--->\n')

        except Exception as e:
            # print(get_bytes(e))
            print(traceback.format_exc())

            break
