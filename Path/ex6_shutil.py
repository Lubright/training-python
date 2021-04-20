from pathlib import Path
import os
from os import path
import shutil

p = Path(__file__)
file_path_parent = p.parent
file_simple_name = p.name

# cp file file_copy
print("shutil copy")

shutil.copy(file_path_parent.joinpath("ex1_basic.py").__str__(), file_path_parent.joinpath("temp").joinpath("ex1_basic_copy.py").__str__())

print("-" * 50 + "\n")

# cp -p
print("shutil copy2")

shutil.copy2(file_path_parent.joinpath("ex1_basic.py").__str__(), file_path_parent.joinpath("temp").joinpath("ex1_basic_copy2.py").__str__())

print("-" * 50 + "\n")


# cp -rfp
print("shutil.copytree()")

if not path.exists(file_path_parent.joinpath("temp2").__str__()): # 不存在，才可建立
    shutil.copytree(file_path_parent.joinpath("temp").__str__(), file_path_parent.joinpath("temp2").__str__(), copy_function=shutil.copy2)

print("-" * 50 + "\n")

# mv
print("shutil.move()")

shutil.move(file_path_parent.joinpath("temp").joinpath("ex1_basic_copy.py").__str__(), file_path_parent.joinpath("temp").joinpath("ex1_basic_copy3.py").__str__())

print("-" * 50 + "\n")

# rm -rf
print("shutil.rmtree()")

if path.exists(file_path_parent.joinpath("temp2").__str__()):
    shutil.rmtree(file_path_parent.joinpath("temp2").__str__())

print("-" * 50 + "\n")
