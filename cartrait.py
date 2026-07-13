class parent_vehicle():

    def __init__(self,brand,color):
        self.brand = brand
        self.color = color

    def show_traits(self):
        print(f"braned: {self.brand}")
        print(f"Color = {self.color}")

class car(parent_vehicle):
    def __init__(self, brand,color,model,engine):
        self.model = model
        self.engine = engine

        super().__init__(brand,color)
        
    def show_traits(self):
        print("name : ", self.model)
        print("age : ",self.engine)
        super().show_traits()



car1 = car("BMW" , "blue", "m4" , "v8")
car1.show_traits()

print(f"Is parent_vehicle subclass of car? : {issubclass(car,parent_vehicle)}")