class dog: 
    species = "4 legged animal"
    def __init__(self,breed,age):
        self.breed = breed
        self.age = age


dog1 = dog("German Shepard", "9")
dog2 = dog("Bulldog", "12")

print(f"dog 1 is a {dog1.species}")
print(f"dog 2 is a {dog2.species}")

print(f"dog 1 is a {dog1.breed} and is {dog1.age} years old")
print(f"dog 1 is a {dog2.breed} and is {dog2.age} years old")

