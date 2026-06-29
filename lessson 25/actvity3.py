class parrot:
    species = "bird"

    def __init__(self,name,age):
        self.name = name
        self.age = age


ob1 = parrot("chew", 7)
ob2 = parrot("pura", 9)

print(f"{ob1.name} is a {ob1.species}")
print(f"{ob2.name} is a {ob2.species}")

print(f"{ob1.name} is {ob1.age} years old")
print(f"{ob2.name} is {ob2.age} years old")