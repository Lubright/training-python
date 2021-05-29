import os
from os import path
from pathlib import Path

p = Path(__file__)
file_path_parent = p.parent
file_simple_name = p.name

files = os.listdir(p.parent)

print(files)

print("-" * 50 + "\n")

def get_file(folderName):
    for e in os.listdir(folderName):
        full_path = path.join(folderName, e)
        if path.isfile(full_path):
            yield full_path
        elif path.isdir(full_path):
            for item in get_file(full_path):
                yield item
            pass

def get_file_2(folderName):
    for e in os.listdir(folderName):
        full_path = path.join(folderName, e)
        if path.isfile(full_path):
            yield full_path
        elif path.isdir(full_path):
            # for item in get_file(full_path):
            #     yield item

            # 簡化
            yield from get_file_2(full_path)


for file_name in get_file(p.parent):
    print(file_name)

print("-" * 50 + "\n")


for file_name in get_file_2(p.parent):
    print(file_name)

print("-" * 50 + "\n")
