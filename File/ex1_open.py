from pathlib import Path

p = Path(__file__)
file_simple_name = p.name
file_path_parent = p.parent

print("file_simple_name:", file_simple_name)
print("file_path_parent:", file_path_parent)
print("-" * 50 + "\n")

content = """Hello Python
中文字測試
Welcome
"""

# ----- write file ----- #
fout = open(file_path_parent.joinpath("ex1_test.txt").__str__(), "wt", encoding="utf-8")
fout.write(content)
fout.close()

print("-" * 50 + "\n")

# ----- read file ----- #
fin = open(file_path_parent.joinpath("ex1_test.txt").__str__(), "rt", encoding="utf-8")
first_5_ch = fin.read(5)
print("first_5_ch:", first_5_ch)

fin.seek(0) # return to original point
doc = fin.read() # read all content
fin.close()

print("doc:", doc)
print("-" * 50 + "\n")

# ----- write file by with ----- #
with open(file_path_parent.joinpath("ex1_test.txt").__str__(), "at", encoding="utf-8") as fout:
    fout.write(content)
print("-" * 50 + "\n")

# ----- read file by with ----- #
with open(file_path_parent.joinpath("ex1_test.txt").__str__(), "rt", encoding="utf-8") as fin:
    doc = fin.read()

    print("current position:", fin.tell())
    fin.seek(0)
    for i, line in enumerate(fin):
        print("{}: {}".format(i+1, line.strip()))

print("doc:", doc)
print("-" * 50 + "\n")




"""
# 若只單純用 open then close 去開關檔案會有記憶體洩漏的風險，例如當檔案讀寫的過程中
發生錯誤而拋出例外，此時很難保證檔案物件有正確被關閉
=> 推薦使用 with open 語法
# 使用 with 可以自動管理資源，無論什麼原因跳出

"""