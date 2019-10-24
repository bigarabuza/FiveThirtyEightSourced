import csv
from pathlib import PurePath
from collections import namedtuple
import numpy as np
import pandas as pd

base_folder = PurePath(__file__).parent
file_name = base_folder.joinpath('data', 'thanksgiving-2015-poll-data.csv')

raw_df = pd.read_csv(file_name)
df_extr_cols = raw_df.iloc[:,np.r_[:2, 63:64, 11:24, 25, 26:37, 38, 40:49, 50]]
col_names = ['income'] + (['sides'] * 14) + (['pie'] * 12) + (['desserts'] * 10)
df_named = df_extr_cols.rename(columns=dict(zip(df1.columns[2:], col_names)))
df = df_named.melt(id_vars=['RespondentID', 'Do you celebrate Thanksgiving?', 'income'], var_name='item', value_name='dish')
df.dropna(subset=['dish'], inplace=True)

print(raw_df.head(3))
print(raw_df.columns[11:50])
print(raw_df.columns[64])