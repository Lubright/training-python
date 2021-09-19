from bank import Bank # 相對式匯入

class Zhongzheng_Bank(Bank):
    """Define Zhongzheng Bank
    """
    def __init__(self, name: str, money: int) -> None:
        super().__init__(name=name, money=money)
        self._title = "Taipei Bank - Zhongzheng Branch"

if __name__ == "__main__":
    print("{} as main program".format(__name__))
    print("-" * 50 + "\n")
else:
    print("{} as module".format(__name__))
    print("-" * 50 + "\n")