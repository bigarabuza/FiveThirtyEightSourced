import csv
from pathlib import PurePath
from collections import namedtuple
import numpy as np
import pandas as pd

base_folder = PurePath(__file__).parent
file_name = base_folder.joinpath('data', 'thanksgiving-2015-poll-data.csv')

raw_df = pd.read_csv(file_name)

#Extract relevant columns, categorize and unpivot data
df_extr_cols = raw_df.iloc[:,np.r_[:2, 64, 63:64, 11:24, 25, 26:37, 38, 40:49, 50]]
col_names = ['region'] + ['income'] +  (['sides'] * 14) + (['pie'] * 12) + (['desserts'] * 10)
df_named = df_extr_cols.rename(columns=dict(zip(df_extr_cols.columns[2:], col_names)))
df = df_named.melt(id_vars=['RespondentID', 'Do you celebrate Thanksgiving?', 'region', 'income'], var_name='item', value_name='dish')
df.dropna(subset=['dish'], inplace=True)


def prompt_user_selection(regions=df.region.unique(), income=df.income.unique()):
    region_options = dict(enumerate(regions, 1))
    income_options = dict(enumerate(income, 1))
    usr_selection = []
    print('Select region from list below:')
    #Region selection
    for key, value in region_options.items():
        print(f'{key}. {value}')
    while True:
        try:
            i = int(input('Enter number: '))
            usr_selection.append(region_options[i])
            break
        except ValueError:
            print('Please enter valid number.')
        except KeyError:
            print('Please enter valid number from options above')
    #Income selection
    print('Select income category from list below:')
    for key, value in income_options.items():
        print(f'{key}. {value}')
    while True:
        try:
            i = int(input('Enter number: '))
            usr_selection.append(income_options[i])
            break
        except ValueError:
            print('Please enter valid number.')
        except KeyError:
            print('Please enter valid number from options above')
    
    return usr_selection

user_selection = prompt_user_selection()

print(df[(df.region == user_selection[0]) & (df.income == user_selection[1])].sample(5)['dish'].tolist())
