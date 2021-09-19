keys = ("Name", "Age")
values = ("Amy", 20)

# zip
player1 = zip(keys, values)
print("player1 = {}, type = {}".format(player1, type(player1)))

player1 = tuple(player1)
print("player1 = {}, type = {}".format(player1, type(player1)))

print("-" * 50 + "\n")

# unzip
k, v = zip(*player1)
print("k = {}, v = {}".format(k, v))

print("-" * 50 + "\n")

# zip used in dict
player1_dict = dict(zip(keys, values))
print("player1_dict = {}, type = {}".format(player1_dict, type(player1_dict))) # dict

print("-" * 50 + "\n")
