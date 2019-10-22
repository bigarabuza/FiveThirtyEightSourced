import csv
from pathlib import PurePath
from collections import namedtuple
import numpy as np
import pandas as pd

base_folder = PurePath(__file__).parent
file_name = base_folder.joinpath('data', 'thanksgiving-2015-poll-data.csv')

df = pd.read_csv(file_name)
print(df.head(3))