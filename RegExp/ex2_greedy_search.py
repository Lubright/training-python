import re

# Python 預設為 greedy mode
print("greedy search...")
msg = "son"*5
pattern_re = re.compile(r'(son){3,5}')
matchObj = pattern_re.search(msg) # 預設為 greedy 模式，所以會顯示最多重複的字串
if matchObj:
    print(matchObj.group(0))

print("-" * 50 + "\n")

# non greedy search - 使用 '*?' '+?' '??'
print("non greedy search...")
msg = "son"*5
pattern_re = re.compile(r'(son){3,5}?')
matchObj = pattern_re.search(msg)
if matchObj:
    print(matchObj.group(0))

print("-" * 50 + "\n")

