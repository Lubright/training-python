# ch27_11.py
from PIL import Image

pict = Image.open("rushmore.jpg")                       # 建立Pillow物件
pict.rotate(45).save("out27_11_1.jpg")                  # 旋轉45度
pict.rotate(45, expand=True).save("out27_11_2.jpg")     # 旋轉45度圖像擴充









