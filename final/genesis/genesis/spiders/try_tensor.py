import csv
import pandas as pd

def csv_to_boolean_table(csv_file_path):
    # 读取 CSV 文件
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        
        headers = next(csv_reader)
        len_headers = len(headers)
        print(headers)
        headers_table = {header: i for header,i in zip(headers, range(len_headers))}
        
        for row in csv_reader:
            # print(row)
            # print()
            for value in row:
                pass
    

csv_file_path = '/Users/linto/Codes/project/genesis/genesis/spec_cfp2017_1.csv'

# 调用函数获取布尔表
boolean_table = csv_to_boolean_table(csv_file_path)

# 打印布尔表
for header, values in boolean_table.items():
    # print(f"{header}: {values}")
    print(header)
