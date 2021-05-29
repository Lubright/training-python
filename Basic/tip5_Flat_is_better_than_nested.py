import this

# The zen of Python
print(this)

class Network:
    def is_url_valid():
        return True

    def is_dns_work():
        return True

    def is_user_valid():
        return True
    
# test here, 不推薦使用這種方式
def download_nested():
    if Network.is_url_valid():
        if Network.is_dns_work():
            if Network.is_user_valid():
                print("start downloading...")
            else:
                print("user invalid")
        else:
            print("dns error")
    else:
        print("url invalid")


def download_flat():
    if not Network.is_url_valid():
        print("url_invalid")
        return
    elif not Network.is_dns_work():
        print("dns error")
        return
    elif not Network.is_user_valid():
        print("user invalid")
        return

    print("start downloading...")


download_flat()

