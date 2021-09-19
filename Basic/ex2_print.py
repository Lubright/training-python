import sys

print(100, "多吃水果", "60", sep=" ", end="\n", file=sys.stdout, flush=False)

print("%s 的成績為 %3d" % ("Amy", 80))

print("{:.2f}".format(34.56789))