import os
import json
from pathlib import Path

p = Path(__file__)
file_path_parent = p.parent
file_simple_name = p.name

# read json from file

with open(file_path_parent.joinpath("test1.json"), mode="rt", encoding="utf-8") as fin:
    json_data = json.load(fin)

print(json_data, type(json_data))
print("-" * 50 + "\n")

# write json to file

with open(file_path_parent.joinpath("test2.json"), mode="wt", encoding="utf-8") as fout:
   json.dump(json_data, fout, indent=2)

print("-" * 50 + "\n")
