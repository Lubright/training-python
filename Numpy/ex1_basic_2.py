import numpy as np

# 資料類型 - 單一資料類型
# dtype=int32
print("資料類型...\n")

int_np_arr = np.array(list(range(1, 4)))
print(int_np_arr, "dtype=", int_np_arr.dtype)

# int_np_arr = np.array(list(range(1, 4)), dtype="int31") # error

int_np_arr = np.array(list(range(1, 4)), dtype="int64")
print(int_np_arr, "dtype=", int_np_arr.dtype)
print("-" * 50 + "\n")

# dtype=float64
float_np_arr = np.array(list(range(1, 4)), dtype="float")
print(float_np_arr, "dtype=", float_np_arr.dtype)
print("-" * 50 + "\n")

# dtype=cpmplex
complex_np_arr = np.array(list(range(1, 4)), dtype=complex)
print(complex_np_arr, "dtype=", complex_np_arr.dtype) # complex128
print("-" * 50 + "\n")

# dtype=bool
bool_np_arr = np.array([-3, -2, -1, 0, 1, 2, 3], dtype=bool)
print(bool_np_arr, "dtype=", bool_np_arr.dtype) # bool
print("-" * 50 + "\n")

# dtype=str
str_np_arr = np.array([0, 1, 2, True, False], dtype=str)
print(str_np_arr, "dtype=", str_np_arr.dtype) # str
print("-" * 50 + "\n")

# 型別轉換 - astype
print("型別轉換 - astype...\n")

result = float_np_arr.astype(int) # 回傳新的物件
print(float_np_arr, "dtype=", float_np_arr.dtype) # float64
print(result, "dtype=", result.dtype) # int
print("-" * 50 + "\n")

# 練習 - filtering
print("練習 - filtering...\n")

age = [19, 21, 20, 19, 21, 17, 30, 36, 90]
age_np_arr = np.array(age)
result = age_np_arr[ (age_np_arr<20) | (age_np_arr>30) ] # 不能用 or, and, 只能用 | or &
print(result, "dtype=", result.dtype)

result = age_np_arr[ (age_np_arr>=20) & (age_np_arr<=30) ] # 不能用 or, and, 只能用 | or &
print(result, "dtype=", result.dtype)
print("-" * 50 + "\n")

# 練習從五人中選出 BMI > 21 的元素
print("練習從五人中選出 BMI > 21 的元素...\n")

names = ['Alex','Bob','Calvin','Derrick','Eric']
heights = [173, 168, 171, 189, 179]
weights = [65.4, 59.2, 63.6, 88.4, 68.7]

name_np_arr = np.array(names)
height_np_arr = np.array(heights, dtype=float)
weight_np_arr = np.array(weights, dtype=float)
bmi_result = weight_np_arr / ((height_np_arr / 100.0) ** 2)
print(bmi_result, "dtype=", bmi_result.dtype)

name_np_arr = name_np_arr[ bmi_result>21 ]
bmi_result = bmi_result[ bmi_result>21 ]
print(name_np_arr, "dtype=", name_np_arr.dtype)
print(bmi_result, "dtype=", bmi_result.dtype)
print("-" * 50 + "\n")


## 練習使用布林選出 Matthew Perry 與 Lisa Kudrow
## uisng np.isin
print("練習使用布林選出 Matthew Perry 與 Lisa Kudrow...\n")

friends_stars = ["Jennifer Aniston", "Courteney Cox", "Lisa Kudrow",
"Matt LeBlanc", "Matthew Perry", "David Schwimmer"]

friends_star_np_arr = np.array(friends_stars)
result = friends_star_np_arr[ (friends_star_np_arr == "Matthew Perry") | (friends_star_np_arr == "Lisa Kudrow") ]
print(result, "dtype=", result.dtype)

result = np.isin(friends_star_np_arr, ["Matthew Perry", "Lisa Kudrow"])
print(result, "dtype=", result.dtype)
print("-" * 50 + "\n")

## 常用屬性與方法
### 元素個數: .size
### 外觀: .shape
### 維度: .ndim
print("常用屬性與方法...\n")

numOfElements = len(friends_star_np_arr)
print("numOfElements:", numOfElements)

print("friends_star_np_arr.size:", friends_star_np_arr.size)
print("friends_star_np_arr.shape:", friends_star_np_arr.shape)
print("friends_star_np_arr.ndim:", friends_star_np_arr.ndim) # 維度
print("-" * 50 + "\n")

# 二維 nparray
print("二維 nparray...\n")

my_2d_np_arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print("my_2d_np_arr:", my_2d_np_arr)
print("my_2d_np_arr.size:", my_2d_np_arr.size)
print("my_2d_np_arr.shape:", my_2d_np_arr.shape) # (2, 3)
print("my_2d_np_arr.ndim:", my_2d_np_arr.ndim) # 2
print("-" * 50 + "\n")

# 使用 reshape
my_2d_np_arr = np.array(list(range(1, 7))).reshape(2, 3)
print("my_2d_np_arr:", my_2d_np_arr)
print("my_2d_np_arr.size:", my_2d_np_arr.size)
print("my_2d_np_arr.shape:", my_2d_np_arr.shape) # (2, 3)
print("my_2d_np_arr.ndim:", my_2d_np_arr.ndim) # 2
print("-" * 50 + "\n")

# 三維 nparray
print("三維 nparray...\n")

# 使用 reshape
my_3d_np_arr = np.array(list(range(1,25))).reshape(2, 3, 4)
print(my_3d_np_arr)
print("my_3d_np_arr.size:", my_3d_np_arr.size)
print("my_3d_np_arr.shape:", my_3d_np_arr.shape) # (2, 3, 4)
print("my_3d_np_arr.ndim:", my_3d_np_arr.ndim) # 3
print("-" * 50 + "\n")

# 轉置
print("轉置...\n")

result = my_2d_np_arr.transpose()
print(result)
print("result.shape:", result.shape)

# indexing
print("indexing...\n")
print("my_2d_np_arr:", my_2d_np_arr)
print(my_2d_np_arr[0])
print(my_2d_np_arr[1][2])
print(my_2d_np_arr[1, 2])
print("-" * 50 + "\n")

print("my_3d_np_arr:", my_3d_np_arr)
print(my_3d_np_arr[1, 1, 1])
print("-" * 50 + "\n")

# filtering
print("filtering...\n")

result = my_3d_np_arr[my_3d_np_arr%5 == 0]
print("result:", result)
print("-" * 50 + "\n")

# 攤平
print("攤平...\n")

result = my_3d_np_arr.ravel()
print("my_3d_np_arr:", my_3d_np_arr)
print("result:", result)
print("-" * 50 + "\n")

result = my_3d_np_arr.reshape(my_3d_np_arr.size,)
print("result:", result)
print("-" * 50 + "\n")

# 依條件取代 - where
print("依條件取代 - where...\n")
result = np.where(my_3d_np_arr%5 == 0, True, False)
print(result)

# 運算
print("運算...\n")
print(my_2d_np_arr)
print("my_2d_np_arr + 2:", (my_2d_np_arr + 2))
print("my_2d_np_arr * 2:", (my_2d_np_arr * 2))
print("my_2d_np_arr / 2:", (my_2d_np_arr / 2))
print("my_2d_np_arr ** 2:", (my_2d_np_arr ** 2))

print("-" * 50 + "\n")

# 矩陣運算
print("矩陣運算...\n")

my_2d_np_arr_T = my_2d_np_arr.transpose()
print(my_2d_np_arr)
print(my_2d_np_arr_T)
result = my_2d_np_arr.dot(my_2d_np_arr_T)

print("result:", result)

print("-" * 50 + "\n")

# vector
print("vector...\n")

my_2d_np_arr # matrix, number of columns > 1
result = my_2d_np_arr.reshape(6, 1) # vector, number of columns == 1
print("result:", result)
print("result.shape:", result.shape)
print("-" * 50 + "\n")

## ndarray 的運算 (4)
### 練習計算 $$u^Tv$$
u = np.array([4, -4, -3]).reshape(3, 1)
v= np.array([4, 2, 4]).reshape(3, 1)
print("u:", u)
print("v:", v)
print("u.T.dot(v):", (u.T.dot(v)))

print("-" * 50 + "\n")

## ndarray 的運算 (5)
### 練習計算 *AI* 與 *IA*
A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
A = np.array(list(range(1, 10))).reshape(-1, 3) # -1: 自動運算
I = np.eye(3) # 單位矩陣
print("A:", A)
print("I:", I)
print("A.dot(I):", (A.dot(I)))
print("I.dot(A):", (I.dot(A)))
print("-" * 50 + "\n")

### 練習計算 *AB* 與 *BA*
A = np.array([
    [1,2],
    [4,5]
])
B = np.array([
    [4,3],
    [2,1]
])

print("A.dot(B):", A.dot(B))
print("B.dot(A):", B.dot(A))
print("-" * 50 + "\n")
