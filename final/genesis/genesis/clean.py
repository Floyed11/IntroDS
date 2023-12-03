import pandas as pd

def temp(x):
    if(len(x["L3"].split(' ')) > 8):
        return x["L3"].split(' ')[7] + ' ' + x["L3"].split(' ')[8] + ' ' + x["L3"].split(' ')[11]
    else:
        return False

csv_file_path = './spider_spec_cfp2017.csv'
data = pd.read_csv(csv_file_path)

data = data.assign(L1_D = lambda x:x["Cache L1"].str.split(' ').str[0] + ' ' + x["Cache L1"].str.split(' ').str[1],
                   L1_I = lambda x:x["Cache L1"].str.split(' ').str[4] + ' ' + x["Cache L1"].str.split(' ').str[5])
del data["Cache L1"]

data = data.assign(L2_ID = lambda x:x["L2"].str.split(' ').str[0] + ' ' + x["L2"].str.split(' ').str[1])
del data["L2"]

data = data.assign(L3_ID = lambda x:x["L3"].str.split(' ').str[0] + ' ' + x["L3"].str.split(' ').str[1])
data.loc[:, "L3_shared"] = data.apply(temp, axis=1)
del data["L3"]

data.to_csv('clean.csv', index=False)
