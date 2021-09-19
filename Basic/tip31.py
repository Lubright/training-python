# 有點問題
fout = open("hello.txt", "wt", encoding="utf-8")
fout.write("hello world") # 這邊可能會出錯，造成無法 close
fout.close()


print("-" * 50 + "\n")

# 使用 try-except
fout = open("hello2.txt", mode="wt", encoding="utf-8")
try:
    fout.write("hello world")
finally:
    fout.close()

print("-" * 50 + "\n")

# 使用 with

with open("hello3.txt", mode="wt", encoding="utf-8") as fout:
    fout.write("hello world")

# 自動 close

print("-" * 50 + "\n")

# 自己實作， with statement context managers

class MyFile:

    def __init__(self, name) -> None:
        self.name = name
        self.file = None
    
    def __enter__(self):
        self.file = open(self.name, mode="wt", encoding="utf-8")
        return self.file
    
    def __exit__(self, exc_type, exc_value, traeback):
        if self.file:
            self.file.close()

with MyFile("hello4.txt") as fout:
    fout.write("hello world")


print("-" * 50 + "\n")


# 自己實作: contextlib

"""
https://docs.python.org/3/library/contextlib.html
"""

from contextlib import contextmanager

@contextmanager
def open_file(name):
    # Code to acquire resource, e.g.:
    # resource = acquire_resource(*args, **kwds)
    f = open(name, mode="wt", encoding="utf-8")
    try:
        yield f
    finally:
        # Code to release resource, e.g.:
        # release_resource(resource)
        f.close()

# >>> with managed_resource(timeout=3600) as resource:
# ...     # Resource is released at the end of this block,
# ...     # even if code in the block raises an exception

with open_file("hello5.txt") as fout:
    fout.write("test1\n")
    fout.write("test2")

