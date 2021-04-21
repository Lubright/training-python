fileName = __file__

try:
    with open(fileName, mode="r", encoding="utf-8") as fin:
        data = fin.read()
except FileNotFoundError as e:
    print(e)
else:
    word_list = data.split()
    print("{} 文章的單字共有{}個".format(fileName, len(word_list)))