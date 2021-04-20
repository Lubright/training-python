from pathlib import Path

p = Path(__file__)
file_path_parent = p.parent

# print self
with open(__file__, mode="rt", encoding="utf-8") as fin:
    for line in fin: # read line
        print(line, end="")