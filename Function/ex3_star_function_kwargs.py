# 使用 ** 建立可變參數函式
def formMolecules(**kwargs):
    if len(kwargs) == 2 and kwargs["hydrogen"] == 2 and kwargs["oxygen"] == 1:
        return "water"
    elif len(kwargs) == 1 and kwargs["unobtanium"] == 12:
        return "aether"

print(formMolecules(hydrogen=2, oxygen=1))
print(formMolecules(unobtanium=12))
print(formMolecules(**{
    "hydrogen": 2,
    "oxygen": 1
}))

# 使用 * 和 ** 建立包裝函式
def printLower(*args, **kwargs):
    args = list(args) # 讓他為list
    for i, s in enumerate(args):
        args[i] = str(s).lower()
    print(*args, **kwargs)

name = "Amy"
printLower("Hello,", name)

printLower(*list("ABC"), sep=", ")

