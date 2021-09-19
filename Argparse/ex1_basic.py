import argparse
import os
from pathlib import Path

p = Path(__file__)
file_path_parent = p.parent
file_simple_name = p.name

argparser = argparse.ArgumentParser(prog=file_simple_name, 
                                    description="description1",
                                    epilog="這是寫在 help 頁面最後面的句子")

argparser.add_argument("arg1", help="這是第一個參數", type=str) # Positional Argument
argparser.add_argument("arg2", nargs=1, help="這是第二個參數", type=str) # Positional Argument
argparser.add_argument("-a", "--arg3", help="這是第三個選項引數", type=str) # Optional Argument
argparser.add_argument("--verbose", action="store_true", help="這是第四個選項引數") # store_true

args = argparser.parse_args()

print("args:", args)
print("arg1:", args.arg1)
print("arg2:", args.arg2)
print("arg3:", args.arg3)
print("verbose:", args.verbose)