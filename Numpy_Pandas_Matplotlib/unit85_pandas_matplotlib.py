import pandas as pd
import matplotlib.pyplot as plt

"""
基本 pandas, matplotlib 操作
"""

# read_csv data
print("read_csv data...\n")

csv_data = pd.read_csv(r'https://storage.googleapis.com/learn_pd_like_tidyverse/gapminder.csv')
print(csv_data.head())
print("-" * 50 + "\n")

# scatter
print("scatter...\n")

x = csv_data["gdpPercap"]
y = csv_data["lifeExp"]
plt.scatter(x=x, y=y)
plt.grid(True)
plt.show()
print("-" * 50 + "\n")

# bar plot
print("bar plot...\n")

y = csv_data.groupby("continent").count()
y = y["country"]
print(y)

x = range(y.size)
labels = y.index
plt.bar(x=x, height=y)
plt.xticks(x, labels)
plt.grid(True)
plt.show()

print("-" * 50 + "\n")

# histogram
x = csv_data["gdpPercap"]
plt.hist(x, bins=30)
plt.grid(True)
plt.show()
print("-" * 50 + "\n")

# line plot
csv_data_tw = csv_data[csv_data["country"]=="Taiwan"]
csv_data_jp = csv_data[csv_data["country"]=="Japan"]
csv_data_cn = csv_data[csv_data["country"]=="China"]
x = csv_data_tw["year"]
y = csv_data_tw["gdpPercap"]
y2 = csv_data_jp["gdpPercap"]
y3 = csv_data_cn["gdpPercap"]
plt.plot(x, y, label="csv_data_tw")
plt.plot(x, y2, label="csv_data_jp")
plt.plot(x, y3, label="csv_data_cn")
plt.legend(loc="lower right")
plt.grid(True)
plt.show()
print("-" * 50 + "\n")
