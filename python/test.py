# 导入必要的模块
import os
import re
from datetime import datetime

# 获取脚本文件的路径
script_path = os.path.dirname(os.path.abspath(__file__))

# 读取要处理的数据
input_file = os.path.join(script_path, "input.txt")
with open(input_file, 'r') as file:
    lines = file.readlines()

# 处理日期和MAC地址数据
date_pattern = r'\b\w+\s+\d{1,2},\s+\d{4}\b'
processed_lines = []  # 存储处理后的行
duplicate_lines = []  # 存储重复的行
for line in lines:
    parts = line.strip().split(' ')
    if len(parts) < 2:
        continue

    date_match = re.search(date_pattern, line)
    if date_match:
        mac_address = parts[0].upper()
        date_str = date_match.group()
        try:
            date_obj = datetime.strptime(date_str, '%B %d, %Y').date()
            formatted_date = date_obj.strftime('%Y-%m-%d')
            processed_line = '  ' + formatted_date + '  ' + mac_address + '\n'
            if line not in processed_lines:  # 检查原始行是否已存在于列表中
                processed_lines.append(line)  # 将原始行添加到processed_lines列表中
            else:
                if line not in duplicate_lines:  # 检查原始行是否已存在于重复行列表中
                    duplicate_lines.append(line)  # 将原始行添加到duplicate_lines列表中
        except ValueError:
            continue

# 构建输出文件的完整路径
output_file = os.path.join(script_path, "output.txt")

# 将处理结果写入文件
output = ''.join(processed_lines)
with open(output_file, 'w') as file:
    file.write(output)

# 输出重复的行到屏幕上
if duplicate_lines:
    print("重复的行：")
    for line in duplicate_lines:
        print(line.strip())

print("处理结果已保存到 " + output_file)