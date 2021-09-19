list1 = list(range(1, 11))

def is_odd(num):
    return num %2 == 1

# filter
odd_numbers = filter(is_odd, list1)
odd_numbers = list(odd_numbers)
print(odd_numbers)
print("-" * 50 + "\n")

# map
list2 = list(map(lambda x: x*2, odd_numbers))
print(list2)

print("-" * 50 + "\n")

# filter with lambda

odd_numbers = list( filter(lambda x: x%2 == 1, list1 ) )
print(odd_numbers)

print("-" * 50 + "\n")


print("-" * 50 + "\n")
print("-" * 50 + "\n")
