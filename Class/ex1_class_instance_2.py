class Animal:
    def __init__(self, name, age=1):
        self.name = name
        self.age = age
    def sing(self):
        print(self.name + " " + str(self.age) + "歲，很會唱歌!")
    def grow(self, year=1):
        self.age += year

bird1 = Animal("bird1")
bird1.grow()
bird1.sing()
bird2 = Animal("bird2", 2)
bird2.grow()
bird2.sing()