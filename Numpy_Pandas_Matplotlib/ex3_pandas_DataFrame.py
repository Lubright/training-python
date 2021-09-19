import pandas as pd

# DataFrame
## 
# 初始化 DataFrame
print("初始化 DataFrame...\n")

df = pd.DataFrame() # 初始化
print(df, type(df))
print("-" * 50 + "\n")

# assign column
print("assign column...\n")

df["position"] = ["PG", "SG", "SF", "PF", "C"]
df["name"] = ['Steve Nash', 'Paul Pierce', 'Dirk Nowitzski', 'Kevin Carnett', 'Shaquille O\'Neal']
print(df, type(df))
print("-" * 50 + "\n")

# df.shape
print("df.shape...\n")

print("df.shape:", df.shape) # (5, 2)
print("-" * 50 + "\n")

# df.index
print("df.index...\n")

index_list = list(df.index)
print("index_list:", index_list)
print("-" * 50 + "\n")

# modify index
print("modify index...\n")

df.index = [13, 34, 41, 21, 34]
print(df, type(df))
print("-" * 50 + "\n")

# reset index
print("reset index...\n")

df = df.reset_index()
print(df, type(df))
print("-" * 50 + "\n")

# modify column name
print("modify column name...\n")

print("df.columns:", df.columns)
df.columns = ["jersey", "position", "name"] # update column name
print(df, type(df))
print("-" * 50 + "\n")

# -------------------------------


# use DataFrame
print("use DataFrame...\n")

fav_players = ['Steve Nash', 'Michael Jordan', 'Dirk Nowitzski', 'Kevin Carnett', 'Shaquille O\'Neal'] # list
positions = ["PG", "SG", "SF", "PF", "C"]
df = pd.DataFrame()
df["position"] = positions
df["name"] = fav_players
print(df, type(df))
print("-" * 50 + "\n")

# selection
print("selection...\n")

print(df["position"], type(df["position"])) # Series

# data = df[df["position"]=="PG"]
# print(data["position"], type(data["position"]))

# input()
# print(data[["position"]], type(data[["position"]]))

# input()

# 可以使用 . 去選擇
print(df.position, type(df.position))
print(df.name, type(df.name))
print("-" * 50 + "\n")

# access data
print("access data...\n")

print(df.name[0])
print(df["name"][0])
print("-" * 50 + "\n")

# 透過像是 [m, n] 選擇資料
## df.loc[m,n]
## df.iloc[m,n]
print("透過像是 [m, n] 選擇資料...\n")
df.index = [13, 23, 41, 21, 34]
print(df, type(df))

print("df.loc[index, column_name]:", df.loc[23, "name"]) # 使用 index, column
print("df.iloc[1,1]:", df.iloc[1][1])
print("row:", df.loc[23,:], sep="\n") # row
print("row:", df.loc[[13, 23],:], sep="\n")
print("-" * 50 + "\n")

# Gapminder 練習
print("Gapminder 練習...\n")

csv_file = r"https://storage.googleapis.com/learn_pd_like_tidyverse/gapminder.csv"
csv_data = pd.read_csv(csv_file)
print(csv_data, type(csv_data))
print("-" * 50 + "\n")

# shape
print("shape:", csv_data.shape) # row, column
print("head:", csv_data.head(5))
print("-" * 50 + "\n")
print("tail:", csv_data.tail(5))
print("-" * 50 + "\n")

# info
print("info:", csv_data.info(), sep="\n")
print("-" * 50 + "\n")

# describe
print("describe:", csv_data.describe(), sep="\n")
print("-" * 50 + "\n")

## 基礎的 DataFrame 用法
### -filter
### -select
### -arrange
### -mutate
### -summarise
### -group by

# filter - 針對觀測值做篩選
print("filter...\n")

result = csv_data[csv_data["country"] == "Taiwan"]
print("result:", result, type(result), sep="\n")
print("-" * 50 + "\n")

# select - 針對變數做選擇
print("select...\n")

result = csv_data[csv_data["country"] == "Taiwan"][["year", "gdpPercap"]]
result = csv_data[csv_data["country"] == "Taiwan"].loc[:,"year":"gdpPercap"]
print("result:", result, type(result), sep="\n")
print("-" * 50 + "\n")

# arrange - 針對變數做排序
print("arrange...\n")

## .sort_index()
result = result.sort_index(ascending=False)
print("result:", result, type(result), sep="\n")
print("-" * 50 + "\n")

## .sort_values()
result = result.sort_values(by="year", ascending=False)
print("result:", result, type(result), sep="\n")
print("-" * 50 + "\n")

# mutate - 新增(衍生)變數
print("mutate...\n")

result["pop_in_million"] = (result["pop"] / 1000000).round(2)
print("result:", result, type(result), sep="\n")
result["Region"] = "North East Asia"
print("result:", result, type(result), sep="\n")
print("-" * 50 + "\n")

# Series.str.split
print("Series.str.split...\n")

ser1 = pd.Series(["3008 abc", "6409 xyz"])
ser2 = ser1.str.split()
print(ser2)
ser2 = ser1.map(lambda s1: s1.split()[0])
print(ser2)
ser3 = ser1.map(lambda s1: s1.split()[1])
print(ser3)
print("-" * 50 + "\n")

# summarise
print("summarise...\n")

csv_file = r"https://storage.googleapis.com/learn_pd_like_tidyverse/gapminder.csv"
csv_data = pd.read_csv(csv_file)
print(csv_data.head(5))
print("-" * 50 + "\n")

print("shape:", csv_data.shape)

result =csv_data["pop"].sum() # 總和
print("pop_sum:", result)

# 2007 pop 總和
print(csv_data["year"].dtype)
result = csv_data[csv_data["year"]==2007]["pop"].sum()
print("result:", result)
print("-" * 50 + "\n")

# 2007 gdpPercap max
max_gdpPercap = csv_data[csv_data["year"]==2007]["gdpPercap"].max()
min_gdpPercap = csv_data[csv_data["year"]==2007]["gdpPercap"].min()
print("max_gdpPercap:", max_gdpPercap)
print("min_gdpPercap:", min_gdpPercap)
print("-" * 50 + "\n")

row_max_gdpPercap_data = csv_data[csv_data["gdpPercap"]==max_gdpPercap]
print("row_max_gdpPercap_data:", row_max_gdpPercap_data)
row_min_gdpPercap_data = csv_data[csv_data["gdpPercap"]==min_gdpPercap]
print("row_min_gdpPercap_data:", row_min_gdpPercap_data)
print("-" * 50 + "\n")

max_gdpPercap_country = row_max_gdpPercap_data["country"].iloc[0]
print("max_gdpPercap_country:", max_gdpPercap_country)

min_gdpPercap_country = row_min_gdpPercap_data.loc[335]["country"]
print("min_gdpPercap_country by loc:", min_gdpPercap_country)
min_gdpPercap_country = row_min_gdpPercap_data.iloc[0][0]
print("min_gdpPercap_country by iloc:", min_gdpPercap_country)

print("-" * 50 + "\n")

# max_index
csv_data_2007 = csv_data[csv_data["year"]==2007]
print("max_index:", csv_data_2007["gdpPercap"].idxmax())
max_index = csv_data_2007["gdpPercap"].idxmax()
print(csv_data_2007.loc[max_index, :])
print(csv_data_2007.loc[max_index, "country"])
print("-" * 50 + "\n")

# min_index
print("min_index:", csv_data_2007["gdpPercap"].idxmin())
min_index = csv_data_2007["gdpPercap"].idxmin()
print(csv_data_2007.loc[min_index, :])
print("-" * 50 + "\n")

# set_index - column to index
# csv_data_2007.index = csv_data_2007["country"]
csv_data_2007 = csv_data_2007.reset_index()
csv_data_2007 = csv_data_2007.set_index("country") # 讓哪一欄位的名稱成為 index
print(csv_data_2007.head())
print("-" * 50 + "\n")

csv_data_2007 = csv_data_2007.reset_index()
print(csv_data_2007.head())
print("-" * 50 + "\n")


# group by
print("group by...\n")

# 針對一個變數
grouped = csv_data.groupby(["year"])
result = grouped["pop"]
print("result:", result,type(result))
print("grouped[pop].sum:", result.sum(), sep="\n")
print("-" * 50 + "\n")

# 針對兩個變數
grouped = csv_data.groupby(["year", "continent"])
result = grouped["pop"]
print("grouped[pop].sum:", result.sum(), sep="\n")
print("-" * 50 + "\n")

temp = result.sum()
print(type(temp)) # Series with MultiIndex
print(temp.iloc[0])
print(temp.index) # MultiIndex
print("-" * 50 + "\n")


# 找中位數
result = grouped["gdpPercap"].median()
print("median:", result, sep="\n")
print("-" * 50 + "\n")


"""
# Python 資料分析
## Ben 2018_11_11
## Pandas
- **Pan**el-**Da**ta-Analysi**s**
- **Pan**el-**Da**taFrame-**S**eries

## Series
- `RangeIndex`+`ndarray`
- Custom index+`ndarray`
"""

