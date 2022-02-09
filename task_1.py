import pandas as pd
from pathlib import Path


df = pd.DataFrame({'Name' : 'Joe Bloggs', 'Tutor Group' : '6T1'},index=[0])


sub_folders = ['AoW',
 'CSP',
 'Folder A',
 'Folder B',
 'Folder C',
 'Folder D',
 'Folder E',
 'Folder F']


def create_folders(dataframe, agg_columns, sub_folders, root_path):
 p = Path(root_path)

 series = dataframe[agg_columns].agg('-'.join, 1)

 for person in series:
  trg_path = p.joinpath(person)
  if not trg_path.is_dir():
   trg_path.mkdir(parents=True)

  for path in sub_folders:
   if not trg_path.joinpath(path).is_dir():
    trg_path.joinpath(path).mkdir()