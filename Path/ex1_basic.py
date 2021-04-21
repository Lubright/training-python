import os
from os import path

if path.basename(path.abspath(".")) != "Path":
    os.chdir("Path")

# get current directory
print("cwd:", os.getcwd())
print("-" * 50 + "\n")


# get abspath
print("abspath(.):", path.abspath(".")) # 等同於 os.getcwd()
print("abspath(..)", path.abspath("..")) # 印出上一層工作目錄的絕對路徑
print("abspath(..)", path.abspath(__file__)) # 印出目前檔案的絕對路徑
print("-" * 50 + "\n")

# get basename
print("basename(__file__):", path.basename(__file__))
print("basename(.):", path.basename(path.abspath("..")))
print("-" * 50 + "\n")

# 傳回相對參考路徑
temp_path = path.abspath("..")+os.sep+"File"
print("File abspath:", path.abspath("..")+os.sep+"File")
print("relpath(~/File):", path.relpath(temp_path)) # ../File
print("-" * 50 + "\n")

# check functions

## exists
print("檔案或資料夾存在:", path.exists(__file__))
print("檔案或資料夾存在:", path.exists("xyz"))
print("檔案或資料夾存在:", path.exists(temp_path))
print("-" * 50 + "\n")

## isdir
print("isdir:", path.isdir(__file__))
print("isdir:", path.isdir(temp_path))
print("-" * 50 + "\n")

## isfile
print("isfile:", path.isfile(__file__))
print("isfile:", path.isfile(temp_path))
print("-" * 50 + "\n")

## mkdir
my_dir = "temp"
if not path.exists(my_dir):
    os.mkdir(my_dir)
print("-" * 50 + "\n")

## rmdir: like linux command, 不過底下有檔案無法刪除

print("-" * 50 + "\n")

## chdir: cd
os.chdir(my_dir)
print("cwd:", os.getcwd())
print("-" * 50 + "\n")


# join
file_path_parent = path.abspath(".")
print("join:", path.join(file_path_parent, "xyz.py"))
print("-" * 50 + "\n")

