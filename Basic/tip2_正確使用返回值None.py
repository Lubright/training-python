def test_connection():
    """模擬數據庫連接測試
    """
    return True

def get():
    """模擬數據庫拿資料
    """
    return []
    # return ["user1", "user2"]

def get_user_list():
    if test_connection:
        return get()
    else:
        return None

user_list = get_user_list()
if user_list is None: # 分辨到底是測試連線失敗，還是拿到的空的數據
    print("connection error")
else:
    print('user_list:', user_list)

print("-" * 50 + "\n")
