import sys

print("sys.getdefaultencoding():", sys.getdefaultencoding())
print("-" * 50 + "\n")

# decode: binary to string
data_big5 = b"\xc4\xc4"
print(data_big5, type(data_big5), sep=", ")
print("decode:", data_big5.decode("big5"))
print("-" * 50 + "\n")

# encode: string to binary
data_utf8='闡'
print(data_utf8, type(data_utf8))
print("encode:", data_utf8.encode("big5"))
print("encode:", data_utf8.encode("utf-8"))
print("-" * 50 + "\n")

s1='abc你我他'
print(s1, type(s1))
print("encode:", s1.encode("utf-8"))
print("-" * 50 + "\n")
