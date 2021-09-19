dict1 = {
    "zhao": 68,
    "qian": 80,
    "sun": 72,
    "li": 90,
    "zhou": 83,
    "wu": 79,
    "zheng": 95,
    "wang": 82
}

print(dict1)
print("-" * 50 + "\n")

# sort dict
# dict1.items().sort(key= lambda item : item[0]) # error
dict1_sorted_by_key = sorted(dict1.items(), key= lambda item: item[0], reverse=False)
print(dict1_sorted_by_key)
print("-" * 50 + "\n")

dict1_sorted_by_value = sorted(dict1.items(), key= lambda item: item[1], reverse=True)
dict1_sorted_by_value = dict(dict1_sorted_by_value)
print(dict1_sorted_by_value)
print("-" * 50 + "\n")
