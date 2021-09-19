import pandas as pd
import os
from os import path
from pathlib import Path

p = Path(__file__)
file_path_parent = p.parent
file_simple_name = p.name

# write as xlsx file
print("write as xlsx file...")
xlsx_data_url = "https://storage.googleapis.com/ds_data_import/fav_nba_teams.xlsx"
xlsx_data = pd.read_excel(xlsx_data_url)
print(xlsx_data)
xlsx_data.to_excel( p.parent.joinpath("out.xlsx"), index=False)
