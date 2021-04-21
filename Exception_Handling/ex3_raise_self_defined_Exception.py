def checkPassWord(pwd: str):
    """檢查密碼長度必須是5~8個字元
    """
    lenOfPwd = len(pwd)
    if lenOfPwd < 5:
        raise Exception("密碼長度不足")
    elif lenOfPwd > 8:
        raise Exception("密碼長度太長")
    print("密碼長度正確")

# test here
for pwd in ("aaabbbccc", "aaa", "asdsad"):
    # checkPassWord(pwd)
    try:
        checkPassWord(pwd)
    except Exception as e:
        print(e)

print("-" * 50 + "\n")
