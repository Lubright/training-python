import pandas as pd

# 練習 - 奧運獎牌練習
## 匯入練習資料
print("匯入練習資料 \n")
df = pd.read_csv('https://storage.googleapis.com/py_ml_datasets/olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index) 
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

print(df.shape)
print("-" * 50 + "\n")

# drop
print("drop...\n")
df = df.drop("Totals")

print(df.shape)
print("-" * 50 + "\n")

### 問題一: 哪個國家贏得的夏季奧運金牌數最多
#### 我的作法:
print("問題一: 哪個國家贏得的夏季奧運金牌數最多 \n")

max_index = df["Gold"].idxmax()
print("max_index:", max_index)
print(df.loc["United States",:])
print("-" * 50 + "\n")

##### sort
sort_data = df.sort_values(by="Gold", ascending=False)
print(sort_data.head(3))
print("-" * 50 + "\n")

### 問題二: 哪個國家夏季奧運與冬季奧運的金牌數差距最大？
print("問題二: 哪個國家夏季奧運與冬季奧運的金牌數差距最大？ \n")

temp = (df["Gold"] - df["Gold.1"]).abs()
print(temp)
max_index = temp.idxmax()
print("max_index:", max_index)
print("-" * 50 + "\n")


### 問題三: 哪個國家夏季奧運與冬季奧運的金牌數差距除以總金牌數的比例最大？（僅考慮至少有一個夏季金牌與一個冬季金牌的國家）
print("問題三: 哪個國家夏季奧運與冬季奧運的金牌數差距除以總金牌數的比例最大？（僅考慮至少有一個夏季金牌與一個冬季金牌的國家） \n")

print(df.head())
filtered_df = df[ (df["Gold"] > 0) & (df["Gold.1"] > 0) ]
result_ser = (filtered_df["Gold"] - filtered_df["Gold.1"]).abs() / (filtered_df["Gold"] + filtered_df["Gold.1"])
print(result_ser)
max_index = result_ser.idxmax()
print("max_index:", max_index)
print(df.loc[max_index,:])
print("-" * 50 + "\n")

# ---------------------------------
# 練習 - 美國普查
## 匯入練習資料
print("匯入練習資料 \n")

df = pd.read_csv('https://storage.googleapis.com/py_ml_datasets/census.csv')
print(df.head())
print(df.shape)
print("-" * 50 + "\n")

### 問題一: 哪一個州（state）的郡（county）數最多？（注意 SUMLEV 變數）
print("問題一: 哪一個州（state）的郡（county）數最多？（注意 SUMLEV 變數） \n")

print(df.columns)
print("-" * 50 + "\n")

#### 使用 groupby
county_df = df[df["SUMLEV"]>40]
state_grouped = county_df.groupby("STNAME")
print(state_grouped["COUNTY"].count())
state_ser = state_grouped["COUNTY"].count()
print(state_ser.idxmax())
print("-" * 50 + "\n")

### 問題二: 假如僅考慮每州（state）人口最多的三個郡（county）計算人口總和，哪三個州總和數最多？（利用 CENSUS2010POP 變數）
print("問題二: 假如僅考慮每州（state）人口最多的三個郡（county）計算人口總和，哪三個州總和數最多？（利用 CENSUS2010POP 變數） \n")

#### 我的作法:
county_df = df[df["SUMLEV"]>40]
state_grouped = county_df.groupby(["STNAME", "CTYNAME"])
print(state_grouped["CENSUS2010POP"].sum())
# print(county_df[county_df["STNAME"]=="Alabama"].loc[1,"CENSUS2010POP"])
temp_ser = state_grouped["CENSUS2010POP"].sum()
print(temp_ser, type(temp_ser))
print(temp_ser[("Alabama", ("Autauga County"))])
print(temp_ser.index[0])
# temp_ser.index = temp.index[1]
# temp_ser.index = [ e[1] for e in temp_ser.index]
# print(temp_ser)

state_names_df = df[df["SUMLEV"]==40]
print(state_names_df)

first_max_pop_list = []
for state_name in state_names_df["STNAME"]:
    # print(state_name)
    temp_ser = county_df[county_df["STNAME"]==state_name]["CENSUS2010POP"].sort_values(ascending=False)
    # print(temp_ser)
    # input()
    first_max_pop_list.append(sum(temp_ser.iloc[0:3]))
print(first_max_pop_list)

state_names_df = state_names_df[["STNAME"]]
state_names_df["first_max_pop_list"] = first_max_pop_list
print(state_names_df.sort_values(by="first_max_pop_list", ascending=False))
print(state_names_df.sort_values(by="first_max_pop_list", ascending=False).iloc[0:3,:])
print("-" * 50 + "\n")

### 問題三: 哪個郡（county）在 2010-2015 期間人口改變數量的絕對值最高？（考慮 POPESTIMATE2010 到 POPESTIMATE2015 這六個變數） 提示：如果五年的人口數分別為 100, 120, 80, 105, 100, 130 則人口改變數量的絕對值為 |130-80| = 50
print("問題三: 哪個郡（county）在 2010-2015 期間人口改變數量的絕對值最高？（考慮 POPESTIMATE2010 到 POPESTIMATE2015 這六個變數） 提示：如果五年的人口數分別為 100, 120, 80, 105, 100, 130 則人口改變數量的絕對值為 |130-80| = 50 \n")
#### 我的作法:
county_df = df[df["SUMLEV"]==50]
target_data = county_df.loc[:,"POPESTIMATE2010":"POPESTIMATE2015"]
target_data["CTYNAME"] = county_df["CTYNAME"]
print(target_data.head())
print("-" * 50 + "\n")

POPESTIMATE_MAX_list = []
POPESTIMATE_MIN_list = []
# print(target_data.loc[1,"POPESTIMATE2010":"POPESTIMATE2015"])
for index in target_data.index:
# for index in (1,):
    POPESTIMATE_MAX_list.append(max(target_data.loc[index,"POPESTIMATE2010":"POPESTIMATE2015"]))
    POPESTIMATE_MIN_list.append(min(target_data.loc[index,"POPESTIMATE2010":"POPESTIMATE2015"]))
# print(POPESTIMATE_MAX_list)
# print(POPESTIMATE_MIN_list)

target_data["POPESTIMATE_MAX"] = POPESTIMATE_MAX_list
target_data["POPESTIMATE_MIN"] = POPESTIMATE_MIN_list
result_ser = pd.Series(target_data["POPESTIMATE_MAX"] - target_data["POPESTIMATE_MIN"])
result_ser.index = target_data["CTYNAME"].values
print(result_ser.sort_values(ascending=False).head())
print("-" * 50 + "\n")

result = list(result_ser.sort_values(ascending=False).index)[0:3]
print(result)
print("-" * 50 + "\n")

#### 可以透過 max(axis=1) 找到 row 方向的最大值
print("有效率的做法...\n")

county_df = df[df["SUMLEV"]==50]
target_data = county_df.loc[:,"POPESTIMATE2010":"POPESTIMATE2015"]
target_data.index = county_df["CTYNAME"]
POPESTIMATE_MAX = target_data.max(axis=1)
POPESTIMATE_MIN = target_data.min(axis=1)
print(target_data.max(axis=1).head(3))
print("-" * 50 + "\n")

print(target_data.min(axis=1).head(3))
print("-" * 50 + "\n")

result_ser = POPESTIMATE_MAX - POPESTIMATE_MIN
print(result_ser.sort_values(ascending=False).head(5))
print("-" * 50 + "\n")

### 問題四: 篩選出屬於 REGION 1 或 2、開頭名稱為 Washington 並且 POPESTIMATE2015 大於 POPESTIMATE2014 的郡（county）
print("問題四: 篩選出屬於 REGION 1 或 2、開頭名稱為 Washington 並且 POPESTIMATE2015 大於 POPESTIMATE2014 的郡（county）\n")

county_df = df[df["SUMLEV"]==50]
selected_data_df = county_df[county_df["REGION"].isin([1,2])]
selected_data_df = selected_data_df[selected_data_df["CTYNAME"].str.startswith("Washington")]
print(selected_data_df)
print("-" * 50 + "\n")

selected_data_df = selected_data_df[ selected_data_df["POPESTIMATE2015"] > selected_data_df["POPESTIMATE2014"] ]
print(selected_data_df)
print("-" * 50 + "\n")





print("-" * 50 + "\n")



