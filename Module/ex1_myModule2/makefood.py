def make_icecream(*toppings):
    print("冰淇淋的配料如下")

    for topping in toppings:
        print("---", topping)

def make_drink(drink: str, size: str):
    print("所點飲料如下")
    print("---", drink.title())
    print("---", size.title())