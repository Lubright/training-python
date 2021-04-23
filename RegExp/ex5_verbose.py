import re

msg = '''02-88223349, (02)-26669999, 02-29998888 ext 123, 
         12345678, 02 33887766 ext. 12222
         '''
print(msg)
pattern_str = r"""(
    (\d{2,3}|\(\d{2,3}\))? # 區域號碼 (不一定要有)
    (\s|-)? # 分隔符號
    \d{7,8} # 電話號碼
    (\s+(ext|ext.)\s+\d{2,4})? # 分機號碼
)
"""
pattern_re = re.compile(pattern_str, re.VERBOSE)
match_list = pattern_re.findall(msg)
print("match_list:", match_list)
print("-" * 50 + "\n")