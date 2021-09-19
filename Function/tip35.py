"""
mypy demo
透過 mypy 做檢查
mypy tip35.py

ci
"""

def sum(x: int, y: int) -> int:
    return x + y

if __name__ == "__main__":
    print(sum("1", "2")) # 12, string cast
