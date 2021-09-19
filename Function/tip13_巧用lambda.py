def g(x):
    return x+1

print(g(1))

print("-" * 50 + "\n")

func2 = lambda x: x+1

print(func2(1))

print("-" * 50 + "\n")

func3 = lambda x, y: x+2*y

print(func3(1, 2))

print("-" * 50 + "\n")

def find(data, filter_func):
    result = []
    for e in data:
        if filter_func(e):
            result.append(e)
    
    return result

result = find(list(range(1, 20)), filter_func=lambda x: x%2==0) # 使用 lambda

print("result:", result)

print("-" * 50 + "\n")

data = ["No", "such", "file", "or", "directory", "A", "C"]

data.sort(key=lambda s1: len(s1), reverse=True)

print(data)

print("-" * 50 + "\n")
    