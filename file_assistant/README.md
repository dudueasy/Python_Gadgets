# Apolo的文件小助手

## file_info 文件信息生成器
*  file_info.py 用于对指定路径(绝对路径)下的所有文件进行扫描, 在同一个目录下生成 files_info.txt文件. 该文件保存了目录下所有文件信息的列表, 包括了文件路径和文件大小.
* 使用示例: 
```
欢迎使用apolo的文件小助手
请输入工作目录:
/Volumes/My Passport
工作目录有效, 正在生成文件信息
```

## file_mover 文件转移工具
* file_mover.py 用于从指定路径开始向下搜索, 将符合条件的文件移动到指定的文件夹.
* 使用示例:
```
欢迎使用apolo的文件小助手
请输入工作目录的绝对路径:
/Volumes/My Passport/Music/
/Volumes/My Passport/Music/
工作目录有效
请输入要移动的文件类型(支持文件名, 后缀名和正则表达式):
Jack Johnson
确认处理 Jack Johnson 类型文件? y/n
y
请输入目标路径:
/Volumes/My Passport/test/
/Volumes/My Passport/test/ 路径可用
开始移动文件
工作完成
```