import pandas as pd

# pd.set_option("display.unicode.east_asian_width", True) # 设置列名对齐
# csv_file_path = '/Users/linto/Codes/project/genesis/genesis/spec_cfp2017_1.csv'
csv_file_path = '/Users/linto/Codes/project/clean.csv'
data = pd.read_csv(csv_file_path)
columns = data.columns

columns_num_flag = {columns[i]: False for i in range(len(columns))}
columns_num_flag['Max MHz'] = True
columns_num_flag['Nominal'] = True
'''可能使用数值也可能使用布尔'''
# columns_num_flag['Cache L1'] = True
# columns_num_flag['L2'] = True
# columns_num_flag['L3'] = True
# columns_num_flag['Memory'] = True
# columns_num_flag['Storage'] = True
columns_num_flag['Cache_L1_I'] = True
columns_num_flag['Cache_L1_D'] = True
columns_num_flag['Cache_L2_ID'] = True
columns_num_flag['Cache_L3_ID'] = True
columns_num_flag['Memory_num'] = True
columns_num_flag['Storage_num'] = True

columns_num_flag['Base Threads'] = True
columns_num_flag['Enabled Cores'] = True
columns_num_flag['Enabled Chips'] = True
columns_num_flag['Threads/Core'] = True
# Cache_L1_I,Cache_L1_D,Cache_L2_ID,Cache_L3_ID,L3_shared,Memory_num,Storage_num
'''分离输入和输出'''
X_num_table = pd.DataFrame()
X_bool_table = pd.DataFrame()
X = data.loc[:, 'Test Sponsor':'Threads/Core']
y = data.loc[:, 'Base Results']
for column in X.columns:
    if columns_num_flag[column]:  
        X_num_table[column] = X[column]
    else:   
        X_bool_table = pd.concat([X_bool_table, pd.get_dummies(X[column])], axis=1)

X_bool_table = X_bool_table.astype(int)
X_after = pd.concat([X_bool_table, X_num_table], axis=1)
X_after.to_csv('output_X.csv', index=False)

y.to_csv('output_y.csv', index=False)

# print(pd.get_dummies(X['Cache L1']))
# print(pd.get_dummies(X['L2']))
# print(pd.get_dummies(X['L3']))
# print(pd.get_dummies(X['Memory']))
# print(pd.get_dummies(X['Storage']))