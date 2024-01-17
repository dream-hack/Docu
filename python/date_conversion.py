# 导入必要的模块
import os  # 导入操作系统模块，用于文件路径操作
import re  # 导入正则表达式模块，用于模式匹配
from datetime import datetime  # 从datetime模块中导入datetime类，用于日期处理

# 获取脚本文件的路径
script_path = os.path.dirname(os.path.abspath(__file__))  # 获取当前脚本文件的绝对路径

# 读取要处理的数据
input_file = os.path.join(script_path, "input.txt")  # 构建输入文件的完整路径
with open(input_file, 'r') as file:  # 打开输入文件，使用'r'模式进行读取
    lines = file.readlines()  # 读取文件的所有行并存储在一个列表中

# 处理日期和MAC地址数据
date_pattern = r'\b\w+\s+\d{1,2},\s+\d{4}\b'  # 定义日期的正则表达式模式
for i, line in enumerate(lines):  # 遍历lines列表中的每一行，同时记录索引和行内容
    parts = line.strip().split(' ')  # 移除行首尾的空白字符，并根据空格拆分行内容，返回一个列表
    if len(parts) < 2:  # 如果列表中的元素少于2个（即不包含日期），则跳过当前行，不进行任何操作
        continue

    date_match = re.search(date_pattern, line)  # 在当前行中搜索日期模式的匹配项
    if date_match:  # 如果找到日期匹配项
        mac_address = parts[0].upper()  # 将列表中的第一个元素转换为大写，作为MAC地址
        date_str = date_match.group()  # 获取日期匹配项的字符串值
        try:
            date_obj = datetime.strptime(date_str, '%B %d, %Y').date()  # 将日期字符串转换为datetime对象，提取日期部分
            formatted_date = date_obj.strftime('%Y-%m-%d')  # 将日期对象格式化为指定格式的字符串
            lines[i] = '  ' + formatted_date + '  ' + mac_address + '\n'  # 在当前行末尾添加格式化后的日期和MAC地址，并添加换行符
        except ValueError:
            continue  # 如果日期格式不正确，则跳过当前行

# 构建输出文件的完整路径
output_file = os.path.join(script_path, "output.txt")  # 构建输出文件的完整路径

# 将处理结果写入文件
output = ''.join(line.rstrip('\n') + '\n' if line.rstrip() else line for line in lines)  # 构建处理结果的字符串，去除每行末尾的换行符，保留原始数据中的换行符
with open(output_file, 'w') as file:  # 打开输出文件，使用'w'模式进行写入
    file.write(output)  # 将处理结果写入文件

print("处理结果已保存到 " + output_file)  # 打印处理结果文件的路径