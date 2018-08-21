# 说明
* python secure shell 模拟器
# 实现功能:
* 通过 python socket 对象来模拟 ssh 客户端和服务器之间的交互. 
* 在 terminal_client 用户界面输入的命令会被传递给 terminal_server 执行
* 服务器通过 subprocess 模块调用 shell 来执行客户端传递的命令, 将命令输出通过 socket 传递会客户端.
# 运行方式:
* 首先执行 terminal_server.py
* 然后执行 terminal_client.py

# 其他
* 请使用 python3 来运行脚本