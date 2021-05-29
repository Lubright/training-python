a = list(range(1, 8))

b = []

for v in a:
    if v%2 == 0:
        b.append(v)

print(b)

print("-" * 50 + "\n")

b = [ v for v in a if v%2==0]
print(b)

print("-" * 50 + "\n")



import time
def calculate_execution_time(func): # decorator function
    def wrapper(*args, **kwargs):
        # t1 = time.time()
        # t1 = time.perf_counter() # 較精確
        t1 = time.perf_counter_ns() # 較精確
        # t1 = time.process_time_ns() # 不包含sleep時間，只計算cpu運算時間
        # print(t1)
        result = func(*args, **kwargs)
        # t2 = time.time()
        # t2 = time.perf_counter()
        t2 = time.perf_counter_ns()
        # t2 = time.process_time_ns()
        # print(t2)

        print("Time elapsed was", (t2 - t1), "ns")
        return result
    return wrapper

@calculate_execution_time
def test_func():
    a = list(range(5000))
    b = []
    for v in a:
        if v%2==0:
            b.append(v)
    # print(b)

# 比較好的做法
@calculate_execution_time
def test_func2():
    a = list(range(5000))
    b = [ e for e in a if e%2==0]
    # print(b)
    
test_func()

print("-" * 50 + "\n")


test_func2()