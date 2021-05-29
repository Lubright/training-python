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

## scatter
print("scatter... \n")

plt.scatter(x=csv_data["gdpPercap"], y=csv_data["lifeExp"], 
c="red",
alpha=0.6,
s=20,
label="gdpPercap", # for legend
marker="+")

plt.title("Gapminder")
plt.xlabel("gdpPercap")
plt.ylabel("lifeExp")
plt.legend(**{
    "loc": "lower right"
})
plt.grid(True)
# plt.show()
print("-" * 50 + "\n")

### 可以重複畫
print("scatter 可以重複畫...\n")

colors = ["red", "green", "blue", "yellow", "pink"]
continents = csv_data["continent"].unique()

for color, continent in zip(colors, continents):
    subset = csv_data[csv_data["continent"]==continent]
    plt.scatter(x=subset["gdpPercap"], y=subset["lifeExp"], 
    c=color,
    alpha=0.6,
    s=20,
    label=continent, # for legend
    marker="+")

plt.title("Gapminder")
plt.xlabel("gdpPercap")
plt.ylabel("lifeExp")
plt.legend(loc="lower right")
plt.grid(True)
# plt.show()
print("-" * 50 + "\n")

## hist
print("hist...\n")

plt.hist(csv_data["gdpPercap"], 
bins=30,
)
plt.grid(True)
# plt.show()
print("-" * 50 + "\n")

### 重複畫
print("hist 重複畫...\n")

colors = ["red", "green", "blue", "yellow", "pink"]
continents = csv_data["continent"].unique()

for color, continent in zip(colors, continents):
    subset = csv_data[csv_data["continent"]==continent]
    plt.hist(subset["gdpPercap"], 
    bins=30, 
    label=continent)

plt.legend(loc="upper right")
plt.grid(True)
# plt.show()
print("-" * 50 + "\n")

## subplots - 重點
print("subplots - 重點...\n")

colors = ["red", "green", "blue", "yellow", "pink"]
fig, axes = plt.subplots(2, 3)

print(axes, type(axes))
print("axes.shape:", axes.shape)

continents = csv_data["continent"].unique()
continents = np.append(continents, [""])
continents = continents.reshape(-1, 3)
print(continents)
print(continents.shape)

for i, r in enumerate(continents):
    for j, continent in enumerate(r):
        if continent == "":
            continue
        subset = csv_data[csv_data["continent"]==continent]
        axes[i, j].hist(subset["gdpPercap"], 
        color=colors.pop(),
        bins=30, 
        label=continent)
        axes[i, j].grid(True)
        axes[i, j].set_title(continent)


axes[1, 2].set_visible(False) # hidden
plt.grid(True)
fig.tight_layout()
plt.show()
print("-" * 50 + "\n")



