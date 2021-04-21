import os
from os import path
from pathlib import Path
import Module.ex1_myModule.lib

p = Path(__file__)
file_path_parent = p.parent
file_simple_name = p.name

print("getsize:", path.getsize(file_path_parent.joinpath("ex1_basic.py").__str__()), "bytes")
