import glob
from pathlib import Path

p = Path(__file__)
file_path_parent = p.parent
file_simple_name = p.name

# list all files
print("all files:", file_path_parent.joinpath("*.*"))
temp = glob.glob(file_path_parent.joinpath("*.*").__str__())
print(temp, type(temp)) # type: list
print("-" * 50 + "\n")

file_list = glob.glob(file_path_parent.joinpath("*.*").__str__())
for file in file_list:
    print(file) # abspath

print("-" * 50 + "\n")

# list all files and directory
file_list = glob.glob(file_path_parent.joinpath("*").__str__())
for file in file_list:
    print(file) # abspath

print("-" * 50 + "\n")
