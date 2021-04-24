import pandas as pd

# Series
print("list...\n")
fav_players = ['Steve Nash', 'Paul Pierce', 'Dirk Nowitzski', 'Kevin Carnett', 'Shaquille O\'Neal'] # list
print("fav_players:", fav_players, type(fav_players))
print("-" * 50 + "\n")

print("Series...\n")
fav_player_ser = pd.Series(fav_players)
print(fav_player_ser, type(fav_player_ser))
print("-" * 50 + "\n")

# values
print("values...\n")
print("fav_player_ser.values:", fav_player_ser.values, type(fav_player_ser.values)) # ndarray
print("-" * 50 + "\n")

# index
print("index...\n")
print("fav_player_ser.index:", fav_player_ser.index, type(fav_player_ser.index))
print("-" * 50 + "\n")

# test multitype data
print("test multitype data...\n")

temp = pd.Series([100, 10.0, "True"])
print(temp, type(temp))
print("temp.values:", temp.values, type(temp.values), "dtype=", temp.values.dtype) # ndarray
print("-" * 50 + "\n")


# traverse values
print("traverse values...\n")

for e in temp.values:
    print(e, type(e))
print("-" * 50 + "\n")

# indexing
print("indexing...\n")
print(fav_player_ser[0])
# print(fav_player_ser[-1]) # error
print("-" * 50 + "\n")

# slice
print("slice...\n")
print(fav_player_ser[0:2])
print("-" * 50 + "\n")

# reverse
print("reverse...\n")
print(fav_player_ser[::-1])
print("-" * 50 + "\n")

# 不規則選取
print("不規則選取...\n")
print(fav_player_ser[[0, 2, 3]])
print("-" * 50 + "\n")

# 調整 index
print("調整 index...\n")
fav_player_ser = pd.Series(fav_players, index=range(1, 6))
print("fav_player_ser:", fav_player_ser, sep="\n")
print("fav_player_ser[1]:", fav_player_ser[1])
print("-" * 50 + "\n")

fav_player_ser = pd.Series(fav_players, index=["PG", "SG", "SF", "PF", "C"]) # 自定義 index
print("fav_player_ser:", fav_player_ser, sep="\n")
print("fav_player_ser[PG]:", fav_player_ser["PG"])
print("-" * 50 + "\n")

# 可以使用 dict 做初始化
fav_player_name_list = ['Steve Nash', 'Paul Pierce', 'Dirk Nowitzski', 'Kevin Carnett', 'Shaquille O\'Neal']
fav_player_position_list = ["PG", "SG", "SF", "PF", "C"]
fav_player_dict = dict(zip(fav_player_position_list, fav_player_name_list))
print("fav_player_dict:", fav_player_dict)
fav_player_ser = pd.Series(fav_player_dict)
print("fav_player_ser:", fav_player_ser, sep="\n")
print("fav_player_ser[PG,SG]:", fav_player_ser[["PG", "SG"]], sep="\n")
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

