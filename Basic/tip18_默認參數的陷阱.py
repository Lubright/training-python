def bad_default_arg(s, times, target=[]):
    for _ in range(times):
        target.append(s)
    return target

result = bad_default_arg(s="a", times=3)

print(result)

print("-" * 50 + "\n")


result = bad_default_arg(s="b", times=3, target=["a"])

print(result)

print("-" * 50 + "\n")

result = bad_default_arg(s="AB", times=2)

print(result) # 有問題

print("-" * 50 + "\n")

result = bad_default_arg(s="CD", times=2)

print(result) # 有問題

print("-" * 50 + "\n")

# 推薦使用方式

def good_default_arg(s, times, target=None):
    if target is None:
        target = [] # initialize list
    for _ in range(times):
        target.append(s)
    return target

result = good_default_arg(s="a", times=3)

print(result)

result = good_default_arg(s="b", times=3)

print(result)