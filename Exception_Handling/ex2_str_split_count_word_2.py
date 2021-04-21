# 分析多個文件的字數

def wordLenOfContent(fileName) -> None:
    try:
        with open(fileName, mode="r", encoding="utf-8") as fin:
            data = fin.read()
    except FileNotFoundError as e:
        print(e)
    else:
        word_list = data.split()
        print("{} 文章的單字共有 {} 個".format(fileName, len(word_list)))


# test here
from pathlib import Path

p = Path(__file__)
file_path_parent = p.parent
file_base_name = p.name
fileName_list = [__file__, file_path_parent.joinpath("ex1_basic.py").__str__(), file_path_parent.joinpath("ex2_str_split_count_word.py").__str__()]

for fileName in fileName_list:
    wordLenOfContent(fileName)
print("-" * 50 + "\n")
