import os
from pathlib import Path
from os import path
import shutil
import re

p = Path(__file__)
file_path_parent = p.parent
file_simple_name = p.name

def get_all_files(filePath, isRecursive: bool = False) -> list:
    fileName_list = []

    for root_dirName, sub_dirNames, fileNames in os.walk(filePath):
        # print("root_dirName:", root_dirName) # list
        # print("sub_dirNames:", sub_dirNames) # list
        # print("fileNames:", fileNames, "\n") # list
        fileNames = map(lambda f: path.join(root_dirName, f), fileNames)
        fileName_list.extend(fileNames)
        # print("fileName_list:", fileName_list, "\n") # list
        if not isRecursive:
            break # do not find file recursively
    
    return fileName_list

fileName_list = get_all_files(file_path_parent, isRecursive=False)
# print("fileName_list:", fileName_list, "\n")

# rename
pattern_re = re.compile(r'([- \w\d]+)(\((\d+)\))?\.\w+$')
numOfFiles = len(fileName_list)
numOfDigits = len(str(numOfFiles))
numOfDigits_str = str(numOfDigits)

for fileName in fileName_list:
    fileName = str(fileName)
    if fileName.endswith(".png"):
        file_root_name, file_ext_name = path.splitext(fileName)

        matchObj = pattern_re.search(fileName)

        file_name_first_part = matchObj.group(1)
        file_default_cnt = matchObj.group(3)

        if file_default_cnt is not None:
            # print(file_default_cnt)
            updated_str = ("{:0"+numOfDigits_str+"d}").format(int(file_default_cnt)+1)
            print("{}({}){}".format(file_name_first_part, updated_str, file_ext_name))
            shutil.move( fileName, "{}({}){}".format(file_name_first_part, updated_str, file_ext_name) )

        else: # 第一個檔案
            updated_str = ("{:0"+numOfDigits_str+"d}").format(1)
            print("{}({}){}".format(file_name_first_part, updated_str, file_ext_name))
            # updated_str = ("{:0"+"2d}").format(2)
            # print(updated_str)
            shutil.move( fileName, "{}({}){}".format(file_name_first_part, updated_str, file_ext_name) )
