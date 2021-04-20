class Animal:
    def __init__(self, weight) -> None:
        self.weight = weight
    def speak(self):
        print("speak...")
    def call_out(self):
        self.speak()
        self.speak()
        self.speak()

class Dog(Animal):
    def __init__(self, weight, name) -> None:
        super().__init__(weight) # 呼叫父類別的 __init__
        self.name = name
    def speak(self):
        print("ARF!!")

dog1 = Dog(2, "Amy")
dog1.call_out()