import re

# test data
msg1 = 'Please call my secretary using 0930-919-919 or 0952-001-001'
msg2 = '請明天17:30和我一起參加明志科大教師節晚餐'
msg3 = '請明天17:30和我一起參加明志科大教師節晚餐, 可用0933-080-080聯絡我'
msg4 = '0952-001-001 請明天17:30和我一起參加明志科大教師節晚餐, 可用0933-080-080聯絡我'

# re.match(pattern, string, flags=0)
print("match...")
pattern_re = re.compile(r"\d{4}-\d{3}-\d{3}")
matchObj = pattern_re.match(msg1)
if matchObj != None:
    print("找到! 電話號碼是: {}".format(matchObj.group()))
else:
    print("{} 不含電話號碼".format(msg1))

matchObj = pattern_re.match(msg2)
if matchObj != None:
    print("找到! 電話號碼是: {}".format(matchObj.group()))
else:
    print("{} 不含電話號碼".format(msg2))


matchObj = pattern_re.match(msg3)
if matchObj != None:
    print("找到! 電話號碼是: {}".format(matchObj.group()))
else:
    print("{} 不含電話號碼".format(msg3))

matchObj = pattern_re.match(msg4)
if matchObj != None:
    print("找到! 電話號碼是: {}".format(matchObj.group()))
else:
    print("{} 不含電話號碼".format(msg4))

print("-" * 50 + "\n")

# 使用 re.search - 指傳回第一個符合的結果
print("search...")
def parsePhoneNumberFromString(s1):
    """解析字串是否含有電話號碼
    """
    pattern_re = re.compile(r"\d{4}-\d{3}-\d{3}")
    matchObj = pattern_re.search(s1)

    if matchObj != None:
        print("找到! 電話號碼是: {}".format(matchObj.group()))
    else:
        print("{} 不含電話號碼".format(s1))

parsePhoneNumberFromString(msg1)
parsePhoneNumberFromString(msg2)
parsePhoneNumberFromString(msg3)
parsePhoneNumberFromString(msg4)
print("-" * 50 + "\n")

# findall - 傳回所有符合結果
print("findall...")
def parsePhoneNumberFromString(s1):
    """解析字串是否含有電話號碼
    """
    pattern_re = re.compile(r"\d{4}-\d{3}-\d{3}")
    phone_list = pattern_re.findall(s1) # 傳回 list
    print("電話號碼是: {}".format(phone_list))

parsePhoneNumberFromString(msg1)
parsePhoneNumberFromString(msg2)
parsePhoneNumberFromString(msg3)
parsePhoneNumberFromString(msg4)
print("-" * 50 + "\n")

# finditer - 傳回所有符合結果
print("finditer...")
msg = 'Please call my secretary using 02-26669999'
pattern_re = re.compile(r'(\d{2})-(\d{7,8})')
match_iter = pattern_re.finditer(msg)
for match in match_iter:
    print(match.group())
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))

print("-" * 50 + "\n")


# group with search
print("group with search...")
msg = 'Please call my secretary using 02-26669999'
pattern_re = re.compile(r"(\d{2})-(\d{7,8})")
matchObj = pattern_re.search(msg)
if matchObj:
    print("group():", matchObj.group())
    print("group(0):", matchObj.group(0))
    print("group(1):", matchObj.group(1))
    print("group(2):", matchObj.group(2))

print("-" * 50 + "\n")

msg = 'Please call my secretary using (02)-26669999'
pattern_re = re.compile(r'\(\d{2}\)-\d{7,8}')
match_list = pattern_re.findall(msg)
print("match_list:", match_list)
print("-" * 50 + "\n")

pattern_re = re.compile(r'\(\d{2}\)-(\d{7,8})')
matchObj = pattern_re.search(msg)
if matchObj:
    print("group():", matchObj.group())
    print("group(0):", matchObj.group(0))
    print("group(1):", matchObj.group(1))

print("-" * 50 + "\n")

# groups - 直接透過 tuple 取得括號內容
print("groups...")
msg = 'Please call my secretary using 02-26669999'
pattern_re = re.compile(r"(\d{2})-(\d{7,8})")
matchObj = pattern_re.search(msg)
if matchObj:
    print("groups():", matchObj.groups())
    print("-" * 50 + "\n")

    areaNum, localNum = matchObj.groups()
    print("areaNum:", areaNum)
    print("localNum:", localNum)

print("-" * 50 + "\n")

# 使用 |
print("使用 |")
msg = 'John and Tom will attend my party tonight. John is my best friend.'
pattern_re = re.compile(r'(John|Tom)')
matchObj = pattern_re.search(msg) # 只會找到 John
if matchObj:
    print("group():", matchObj.group())
    print("group(0):", matchObj.group(0))
    print("group(1):", matchObj.group(1))

match_list = pattern_re.findall(msg)
print("match_list:", match_list)

print("-" * 50 + "\n")

# 使用 | with group
print("使用 | with group")
msg = 'Johnson, Johnnason and Johnnathan will attend my party tonight.'
pattern_re = re.compile(r'John(son|nason|nathan)')
matchObj = pattern_re.search(msg) # 只會找出第一個符合結果
if matchObj:
    print("group():", matchObj.group())
    print("group(0):", matchObj.group(0))
    print("group(1):", matchObj.group(1))

match_list = pattern_re.findall(msg)
print("match_list:", match_list)
print("-" * 50 + "\n")

# ignore case
print("ignore case")
msg = 'john and TOM will attend my party tonight. JOHN is my best friend.'
pattern_re = re.compile(r'John|Tom', re.I)
match_list = pattern_re.findall(msg)
print("match_list:", match_list)
print("-" * 50 + "\n")
