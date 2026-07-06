class vehicle : 
    def __init__(self,milage,max_speed):
        self.milage = milage
        self.max_speed = max_speed

modely = vehicle(10,150)

print(f"the maximum speed of model y is {modely.max_speed}")
print(f"the milage of model y is {modely.milage}")