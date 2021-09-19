class Hi:
    def say(self, name, greeting="hello"):
        print(f"Hi {name}, {greeting}")

hi = Hi()
hi.say(name="Amy", greeting="how are you?")

print("-" * 50 + "\n")

hi.say(name="Justin")

print("-" * 50 + "\n")
