class People:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
    
    def __repr__(self) -> str:
        pass

    # overriding
    def __eq__(self, o: object) -> bool:
        return (self.name == o.name) and(self.age == o.age)
    
p1 = People("Amy", 20)
p2 = People("Amy", 20)

print(p1, p2)
print("p1 == p2?", (p1 == p2) )

print("-" * 50 + "\n")

# dataclass
from dataclasses import dataclass

@dataclass
class NewPeople:
    name: str
    age: int

p1 = NewPeople("Amy", 20)
p2 = NewPeople("Amy", 20)

print(p1, p2)
print("p1 == p2?", (p1 == p2) )
