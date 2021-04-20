import os
from pathlib import Path

p = Path(__file__)
file_path_parent = p.parent
file_simple_name = p.name

# test type
temp = os.walk(file_path_parent)
print(temp, type(temp)) # type: generator
print("-" * 50 + "\n")

# traverse the directory
for root_dirName, sub_dirNames, fileNames in os.walk(file_path_parent):
    print("root_dirName:", root_dirName) # list
    print("sub_dirNames:", sub_dirNames) # list
    print("fileNames:", fileNames, "\n") # list



print("-" * 50 + "\n")
