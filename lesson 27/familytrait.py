class familymember():

    def __init__(self,eye_color,height_cm):
        self.eye_color = eye_color
        self.height_cm = height_cm

    def show_traits(self):
        print(f"Eye Colour: {self.eye_color}")
        print(f"Height(cm) = {self.height_cm}")

class kid(familymember):
    def __init__(self,eye_color,age,height_cm,name):
        self.age = age
        self.name = name

        super().__init__(eye_color,height_cm)
        
    def show_traits(self):
        print("name : ", self.name)
        print("age : ",self.age)
        super().show_traits()

    def fav_hobby(self):
        print("they like football")

class new():
    pass


child = kid("blue" , 15, 167 , "emily")
child.show_traits()
child.fav_hobby()
print(f"Is kid subclass of parent : {issubclass(kid,familymember)}")