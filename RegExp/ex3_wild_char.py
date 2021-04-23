import re, time

msg = 'cat hat sat at matter flat'
pattern_re = re.compile(r'.at', re.IGNORECASE)
t1 = time.perf_counter_ns()
match_list = pattern_re.findall(msg)
t2 = time.perf_counter_ns()
print("match_list:", match_list)
print("Time elapsed was", (t2 - t1), "ns")
print("-" * 50 + "\n")

t1 = time.perf_counter_ns()
match_iter = pattern_re.finditer(msg)
t2 = time.perf_counter_ns()
print("Time elapsed was", (t2 - t1), "ns")
for match in match_iter:
    print(match.group(0))
print("-" * 50 + "\n")
