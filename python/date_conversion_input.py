# 导入必要的模块
import os
from datetime import datetime

# 获取脚本文件的路径
script_path = os.path.dirname(os.path.abspath(__file__))

# 读取要处理的数据
input_file = os.path.join(script_path, "date_conversion_input.txt")
with open(input_file, 'r') as file:
    lines = file.readlines()

# 处理日期和MAC地址数据
for i, line in enumerate(lines):
    parts = line.strip().split(' ')
    mac_address = parts[0]
    date_str = ' '.join(parts[1:])
    date_obj = datetime.strptime(date_str, '%B %d, %Y').date()
    formatted_date = date_obj.strftime('%Y-%m-%d')
    lines[i] = formatted_date + ' ' + mac_address

# 构建输出文件的完整路径
output_file = os.path.join(script_path, "date_conversion_output.txt")

# 将处理结果写入文件
output = '\n'.join(lines)
with open(output_file, 'w') as file:
    file.write(output)

print("处理结果已保存到 " + output_file)