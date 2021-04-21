import traceback

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
        # print(e)
        with open("error.log", "at", encoding="utf-8") as fout:
            fout.write(traceback.format_exc()) # 寫入錯誤
            fout.write("\n")
        print("將 Traceback 寫入錯誤檔案完成...")
        print(e)