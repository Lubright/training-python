import os
from os import path
from pathlib import Path

p = Path(__file__)
file_path_parent = p.parent
file_simple_name = p.name

total_size = 0
for file in os.listdir("."):
    if path.isfile(file):
        print("{} size is {} bytes.".format(file, path.getsize(file)))
        total_size += path.getsize(file)

print("total size is {} bytes.".format(total_size))
