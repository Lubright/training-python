import re

# 不管取代成功與否，都會回傳新字串
msg = 'cat hat sat at matter flat'
pattern_re = re.compile(r'.at')
match_list = pattern_re.findall(msg)
print("match_list:", match_list)
print("-" * 50 + "\n")

print("替換全部")
result = pattern_re.sub("ab", msg)
print("result:", result)
print("-" * 50 + "\n")

print("替換一次")
result = pattern_re.sub("ab", msg, count=1) # 替換一次
print("result:", result)
print("-" * 50 + "\n")

print("替換失敗")
pattern_re = re.compile(r'ab')
result = pattern_re.sub("ab", msg) # 替換失敗
print("result:", result)
print("-" * 50 + "\n")
