import pandas as pd
import glob
import datetime
#last_data = []
# for i in range(6):
#     data_path = glob.glob('./crawling_data/data_{}*'.format(i))[-1]
#     last_data.append(data_path)
# print(data_path)
data_path = glob.glob('./crawling_data/*')
#print(data_path)
#print(len(data_path))

df = pd.DataFrame()
for path in data_path[:-1]:
#for path in last_data:
    df_temp = pd.read_csv(path, index_col=0)
    df_temp.dropna(inplace=True)
    df = pd.concat([df, df_temp])

df_temp = pd.read_csv(data_path[-1])
df = pd.concat([df, df_temp])
print(df.head())
print(df['category'].value_counts())
df.info()
df.to_csv('./naver_new_titles_{}.csv'.format(
    datetime.datetime.now().strftime('%Y%m%d')), index=False)