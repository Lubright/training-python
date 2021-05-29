import numpy as np
import pandas as pd

# Gapminder 資料
print("Gapminder 資料...\n")

csv_file = r"https://storage.googleapis.com/learn_pd_like_tidyverse/gapminder.csv"
csv_data = pd.read_csv(csv_file)
print(csv_data.head())
print("-" * 50 + "\n")

print(csv_data.info())
print("-" * 50 + "\n")

# matplotlib
## - installation: pip install matplotlib
### - plt.scatter() : 散佈圖 (兩個數值)
### - plt.hist() : 直方圖 (一個數值)
### - plt.subplots() : 子圖 (在一個畫布上顯示多個圖形)
### - plt.bar() : 長條圖 (類別, 數值摘要)
### - plt.plot() : 線圖 (一個時間, 一個數值)

import matplotlib.pyplot as plt

## plot
print("plot...\n")

subset = csv_data[csv_data["country"] == "Taiwan"]
plt.plot(subset["year"], subset["lifeExp"])
plt.grid(True)
plt.show()
print("-" * 50 + "\n")

### 重複畫
print("plot 重複畫...\n")

countries = ["Taiwan", "China", "Japan", "Singapore"]
for country in countries:
    subset = csv_data[csv_data["country"] == country]
    plt.plot(subset["year"], subset["lifeExp"], 
    label=country)

plt.legend(loc="lower right")
plt.grid(True)
plt.show()
print("-" * 50 + "\n")


## bar - 長條圖
print("bar - 長條圖...\n")

csv_data_2007 = csv_data[csv_data["year"] == 2007]
grouped = csv_data_2007.groupby("continent")
result_ser = grouped["country"].count()

plt.bar(range(5), result_ser)
plt.xticks(range(5), result_ser.index)
# plt.annotate("52", (0, 52))

for i, v in enumerate(result_ser.values):
    plt.annotate(str(v), (i-0.07, v+1), )

plt.ylim(0, 60)
plt.grid(True)
plt.show()
print("-" * 50 + "\n")



