import zipfile
from pathlib import Path
import os
from os import path


p = Path(__file__)
file_path_parent = p.parent
file_simple_name = p.name

def get_all_file_paths(directory):
    # initializing empty file paths list
    file_paths = []

    # traverse all files
    for root_dirName, sub_dirNames, fileNames in os.walk(directory):
        for fileName in fileNames:
            fileName = path.join(root_dirName, fileName)
            file_paths.append(fileName)
    
    return file_paths

# 壓縮檔案
print("壓縮檔案")

print('Following files will be zipped:')
allFilePaths = get_all_file_paths(file_path_parent.__str__())
with zipfile.ZipFile(file_path_parent.joinpath("out1.zip").__str__(), "w") as fileZipObj:

    for fileName in allFilePaths:
        fileName = path.relpath(fileName, file_path_parent.__str__()) # 使用相對路徑，不然會把絕對路徑資訊也寫進去
        print(fileName)

        # writing files to a zipfile
        fileZipObj.write(fileName)

print('All files zipped successfully!')
print("-" * 50 + "\n")

# 讀取壓縮檔案
print("讀取壓縮檔案")

with zipfile.ZipFile(file_path_parent.joinpath("out1.zip").__str__(), "r") as fileZipObj:
    print(fileZipObj.namelist()) # list: 列出所有壓縮檔案

    print()
    for info in fileZipObj.infolist():
        print(info.filename, info.file_size, info.compress_size, "bytes")

print("-" * 50 + "\n")

# 解壓縮檔案
print("解壓縮檔案")
output_dirName = "out1"
with zipfile.ZipFile(file_path_parent.joinpath("out1.zip").__str__(), "r") as fileZipObj:
    fileZipObj.extractall(output_dirName)

print("-" * 50 + "\n")

# restore
import shutil

os.remove(file_path_parent.joinpath("out1.zip").__str__())
shutil.rmtree(file_path_parent.joinpath("out1").__str__())