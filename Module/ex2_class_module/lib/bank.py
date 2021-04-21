class Bank:
    """定義 Bank 類別
    """
    def __init__(self, name: str = "", money: int = 0) -> None:
        self.__name = name
        self.__balance = money
        self._title = "Taipei Bank" # 模擬 protected member
    
    def save_money(self, money) -> None:
        self.__balance += money
        print("save money done...")

    def withdraw_money(self, money) -> None:
        self.__balance -= money
        print("withdraw money done...")

    def get_balance(self) -> int:
        return self.__balance

    def get_name(self, money) -> str:
        return self.__name
    
    def get_title(self) -> str:
        return self._title
    
    def __str__(self) -> str:
        return "[Bank]: title: {}, name: {}, balance: {}".format(self._title, self.__name, self.__balance)
    

class Shilin_Bank(Bank):
    """Define Shilin Bank
    """
    def __init__(self, name: str, money: int) -> None:
        super().__init__(name=name, money=money)
        self._title = "Taipei Bank - Shilin Branch"
    
    def get_title(self) -> str:
        return self._title

if __name__ == "__main__":
    print("{} as main program".format(__name__))
    print("-" * 50 + "\n")
else:
    print("{} as module".format(__name__))
    print("-" * 50 + "\n")