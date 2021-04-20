import os
from os import path
from pathlib import Path

p = Path(__file__)
file_path_parent = p.parent
file_simple_name = p.name

# get file size
print("getsize:", path.getsize(file_path_parent.joinpath("ex1_basic.py").__str__()), "bytes")
print("-" * 50 + "\n")

# list files
file_list = os.listdir(".")
print("file_list:", file_list)