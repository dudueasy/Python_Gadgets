# -*- coding: utf-8 -*-
# __author__ = 'apolo'
# _date_ = '2018/1/23 上午8:19'

import socket, os

# 初始化工作

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# 自定义一个 bytes 转换器
def get_bytes(n):
    return str(n).encode()


# 创建socket对象
client_sk = socket.socket()

# 连接服务器, 参数为服务器的ip和端口.
address = ('127.0.0.1', 8002)

print('client 开始连接服务器')
client_sk.connect(address)

while True:

    # tips : 命令格式为 post | file_path
    command = input('请输入要执行的命令和文件 : ')
    input_command, input_path = command.split("|")

    # 分割输入为两部分: 命令和文件地址
    input_command = input_command.strip()
    input_path = input_path.strip()

    # 获取文件绝对路径, 文件名, 文件大小
    file_path = os.path.join(BASE_DIR, input_path)
    file_name = os.path.basename(file_path)
    file_size = os.stat(file_path).st_size

    # 封包, 包中包含了文件名和文件大小的数据, 用 | 分割
    file_info = '%s|%s|%s' % (input_command, file_name, file_size)

    client_sk.sendall(file_info.encode())
    print('---信息已发送-->\n')
    client_sk.recv(1024)

    try:
        # 读取并上传对应的文件数据
        # 这里使用  rb 模式读取的数据已经是 bytes类型了.
        with open(file_path, 'rb') as file_obj:

            # 为了减少内存的使用. 我们用while循环来读取数据
            # 每次读取1024个字节. 刚好对应send()每次的发送量
            # 初始化已发送的数量. 用于控制循环
            has_sent = 0
            while has_sent < file_size:
                data = file_obj.read(1024)
                client_sk.sendall(data)
                # print(data)
                # 这里如果要获取数据的大小,应该直接获取 bytes 对象的长度, 如果直接
                has_sent += len(data)


    except Exception as e:
        print(e)

    else:
        print('上传成功')

