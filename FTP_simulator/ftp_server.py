# -*- coding: utf-8 -*-
#!/usr/bin/env python3
__author__ = 'apolo'
_date_ = '2018/1/23 上午8:18'

import socket, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
media_folder = 'media'

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
            print('开始接收文件信息')
            # 获取数据并且转换为unicode格式
            data = conn.recv(1024).decode()

            # 如果没有数据那就直接出本次持续通信, 等待建立新的连接
            if not data:
                break
            input_command, file_name, file_size = data.split('|')
            file_size = int(file_size)
            print('文件大小为 %i'%(file_size))

            conn.send('ready to receive file'.encode())

            # 定义一个媒体文件夹路径
            upload_to = os.path.join(BASE_DIR, media_folder, file_name)
            media_folder = os.path.join(BASE_DIR, media_folder)
            if not os.path.isdir(media_folder):
                os.mkdir(media_folder)

            try:
                # 使用一个 while 循环来持续接收数据并写入文件
                with  open(upload_to, 'ab') as file_obj:
                    received_data_size = 0
                    while received_data_size < file_size:
                        data = conn.recv(1024)
                        file_obj.write(data)
                        received_data_size += len(data)
                        # print('已接收数据 %i字节'%(received_data_size))

            except Exception as e:
                print(e)

            else:
                print('文件接收完成')
        except Exception as e:
            print(e)
            break
