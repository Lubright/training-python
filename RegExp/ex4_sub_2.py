import re

msg = 'CIA Mark told CIA Linda that secret USB had given to CIA Peter.'
pattern_re = re.compile(r'CIA\s(\w)\w+')
match_list = pattern_re.findall(msg)
print("match_list:", match_list)
print("-" * 50 + "\n")

replaceString = r"\1***"
result = pattern_re.sub(replaceString, msg)
print("result:", result)
print("-" * 50 + "\n")