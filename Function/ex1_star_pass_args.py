print("a", "b", "c")

# using list to pass arguments
args1=list("abc")
print(*args1) # using *
print("-" * 50 + "\n")

print("a", "b", "c", sep="-")

kwargs1 = {"sep": "-"}
print(*args1, **kwargs1) # using **
print("-" * 50 + "\n")
