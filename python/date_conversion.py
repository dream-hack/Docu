# 导入必要的模块
from datetime import datetime

data = """
00:1A:79:D5:1B:92 January 28, 2023
00:1A:79:51:6E:08 February 13, 2023
00:1A:79:71:18:A3 January 11, 2023

"""

# 将数据拆分成行
lines = data.strip().split('\n')

# 遍历每一行进行日期转换和替换
for i, line in enumerate(lines):
    parts = line.split(' ')
    date_str = ' '.join(parts[1:])
    date_obj = datetime.strptime(date_str, '%B %d, %Y')
    formatted_date = date_obj.strftime('%Y-%m-%d')
    lines[i] = parts[0] + ' ' + formatted_date

# 打印结果
output = '\n'.join(lines)
print(output)
