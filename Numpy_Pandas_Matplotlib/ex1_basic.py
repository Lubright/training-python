import numpy as np
import pandas as pd
from pathlib import Path

p = Path(__file__)
file_path_parent = p.parent
file_simple_name = p.name

# test pandas
print("test pandas...\n")

csv_file = file_path_parent.joinpath("test_data").joinpath("submission.csv")
csv_data = pd.read_csv(csv_file.__str__())
print(csv_data.head(5))
print("-" * 50 + "\n")

salePrice = csv_data["SalePrice"]
print(salePrice.head(5))
print("-" * 50 + "\n")

# 使用 np.array() 創造
print("使用 np.array() 創造...\n")

arr = np.array(list(range(1,4)))
print(arr, type(arr))
print("-" * 50 + "\n")

# 使用 np.arange()
print("使用 np.arange()...\n")

x1 = np.arange(0, 11, 1)
print(x1, type(x1))
print("-" * 50 + "\n")

# 使用 np.linspace()
print("使用 np.linspace()...\n")

x1 = np.linspace(0, 10, num=11)
print(x1, type(x1)) # 11 float data
print("-" * 50 + "\n")

# 使用 np.ones()
print("使用 np.ones()...\n")

ones_np_arr = np.ones(5)
print(ones_np_arr, type(ones_np_arr))
print("-" * 50 + "\n")

# 型別轉換
print("型別轉換...\n")

x1 = np.linspace(1, 10, num=10, dtype=int)
print(x1)
x1 = np.linspace(1, 10, num=10).astype(int)
print(x1)
print("-" * 50 + "\n")

# list v.s. ndarray
print("list v.s. ndarray...\n")

num_list = list(range(1, 10, 2))
num_np_arr = np.arange(1, 10, 2)
print("num_list:", num_list)
print("num_np_arr:", num_np_arr)
print("-" * 50 + "\n")

print("num_list[0]:", num_list[0])
print("num_np_arr[0]:", num_np_arr[0])
print("-" * 50 + "\n")

print("num_list[-1]:", num_list[-1])
print("num_np_arr[-1]:", num_np_arr[-1])
print("-" * 50 + "\n")

num_list2 = num_list[1:4] # slice
num_np_arr2 = num_np_arr[1:4] # slice
print("num_list2:", num_list2)
print("num_np_arr2:", num_np_arr2)
print("-" * 50 + "\n")

num_list2 = num_list[::-1] # reverse
num_np_arr2 = num_np_arr[::-1] # reverse
print("num_list2:", num_list2)
print("num_np_arr2:", num_np_arr2)
print("-" * 50 + "\n")

# np array dtype 只會有一種
mixed_types_data= [100, 10.0, True, False, "100"]
for e in mixed_types_data:
    print(type(e))

mixed_types_data_np_arr = np.array(mixed_types_data)
print("mixed_types_data_np_arr:", mixed_types_data_np_arr) # dtype=str
print("mixed_types_data_np_arr.dtype:", mixed_types_data_np_arr.dtype) # dtype=str
print("-" * 50 + "\n")

mixed_types_data= [100, 10.0, True, False]
for e in mixed_types_data:
    print(type(e))

mixed_types_data_np_arr = np.array(mixed_types_data)
print("mixed_types_data_np_arr:", mixed_types_data_np_arr) # dtype=float
print("mixed_types_data_np_arr.dtype:", mixed_types_data_np_arr.dtype) # dtype=float
print("-" * 50 + "\n")

# 運算
print("運算...\n")
mixed_types_data = mixed_types_data * 2
print("mixed_types_data:", mixed_types_data)
print("-" * 50 + "\n")

# mixed_types_data = mixed_types_data * 2.5 # error, because of type
# print("mixed_types_data:", mixed_types_data)
# print("-" * 50 + "\n")

# 向量運算
mixed_types_data= [100, 10.0, True, False]
mixed_types_data_np_arr = np.array(mixed_types_data)
result = mixed_types_data_np_arr + 2
print("result:", result) # dtype=float
print("-" * 50 + "\n")

result = mixed_types_data_np_arr * 2
print("result:", result) # dtype=float
print("-" * 50 + "\n")

result = mixed_types_data_np_arr / 2
print("result:", result) # dtype=float
print("-" * 50 + "\n")

# np array 不規則選取
print("np array 不規則選取...\n")

np_arr = np.arange(1, 10, 2)
print("np_arr:", np_arr)

result = np_arr[[1, 3, -1]]
print("result:", result)

print("(np_arr > 5):", (np_arr > 5))

result = np_arr[(np_arr > 5)]
print("result:", result)

result = np_arr[((np_arr % 5) == 0)]
print("result:", result)
print("-" * 50 + "\n")


"""
## Numpy

*   Installation <br>
pip install numpy
*   Numerical Python
*   Import <br>
import numpy s np
*   使用 np.array() 產生 <br>
*   list有但 ndarray 沒有的特性：可容納多種型別
*   ndarray有但 list 沒有的特性：
      - 向量式計算
      - 不規則的 indexing
      - boolean filtering
"""
