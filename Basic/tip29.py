s = " Last Checkpoint: a few seconds ago (unsaved cahnges) "

print(s)

# strip
s = s.strip()
print(s)
print("-" * 50 + "\n")

# lower
s = s.lower()
print(s)

# replace
s = s.replace("(", "#").replace(")", "#")
print(s)
print("-" * 50 + "\n")

# list to string using join
s = ["an", "hours", "age"]
s2 = " ".join(s)
print(s2)

print("-" * 50 + "\n")
print("-" * 50 + "\n")
print("-" * 50 + "\n")
print("-" * 50 + "\n")
print("-" * 50 + "\n")

