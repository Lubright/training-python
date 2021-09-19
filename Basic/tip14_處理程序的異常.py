class Check:

    @staticmethod
    def check_network():
        return True
    
    @staticmethod
    def check_download_url():
        return True
    
    @staticmethod
    def check_access_allowed():
        return True
    
    @staticmethod
    def check_dns():
        # return True
        return False

# 太多 if-else，建議使用 exception
def download_file():
    if not Check.check_network():
        print("Cannot connect to network")
        return

    if not Check.check_download_url():
        print("Invalid URL")
        return

    if not Check.check_access_allowed():
        print("Cannot access resoure (permission denied)")
        return

    if not Check.check_dns():
        print("No DNS")
        return

    return ["c", "o", "o", "l"]

print("-" * 50 + "\n")


# 推薦方式

class ConnectionError(Exception):
    pass

class DownloadURLError(Exception):
    pass

class PermissionError(Exception):
    pass

class DNSError(Exception):
    pass

def download_file_2():
    if not Check.check_network():
        raise ConnectionError("Cannot connect to network")

    if not Check.check_download_url():
        raise DownloadURLError("Invalid URL")

    if not Check.check_access_allowed():
        raise PermissionError("Cannot access resoure (permission denied)")

    if not Check.check_dns():
        raise DNSError("No DNS")

    # test code
    a = 1/0

    return ["c", "o", "o", "l"]


if __name__ == "__main__":

    # print(download_file())
    # print(download_file_2())

    try:
        print(download_file_2())
    except DNSError as e:
        # check configure DNS
        print("xxxx DNS error")
    except Exception as e:
        print(e)