import csv
from pathlib import PurePath
from collections import namedtuple

base_folder = PurePath(__file__).parent
file_name = base_folder.joinpath('data', 'thanksgiving-2015-poll-data.csv')

Record = namedtuple('Record')

with open(file_name, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row.get())