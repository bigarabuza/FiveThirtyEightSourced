import csv
from pathlib import PurePath
from collections import namedtuple
import numpy as np
import pandas as pd

base_folder = PurePath(__file__).parent
file_name = base_folder.joinpath('data', 'thanksgiving-2015-poll-data.csv')

raw_df = pd.read_csv(file_name)
print(raw_df.head(3))
print(raw_df.columns[11:50])
print(raw_df.columns[64])