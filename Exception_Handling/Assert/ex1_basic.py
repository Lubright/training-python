class Bank:
    title = "Taipei Bank" # class variable
    def __init__(self, name: str, money: int = 0) -> None:
        self.__name = name
        self.__money = money
    
    def save_money(self, money):
        assert money > 0, "存款金額要大於0" # 不用寫 if 判斷式和 raise Exception
        self.__money += money
    
    def withdraw_money(self, money):
        assert self.__money < money, "存款金額不足"
        self.__money -= money
    
    def get_balance(self):
        return "{} 目前餘額: {} 元".format(self.__name, self.__money)


# test here
Amy_account = Bank("Amy", 1000)
Amy_account.save_money(-1000) # 停在這邊，因為 AssertionError
Amy_account.withdraw_money(2000)
Amy_account.withdraw_money(500)
Amy_account.get_balance()
print("-" * 50 + "\n")

