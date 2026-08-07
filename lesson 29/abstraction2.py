from abc import ABC , update_abstractmethods

class animal(ABC): 
    def move(self): 
        pass

class human(animal): 
    def move(self):
        print("I can walk and run")

class snake(animal): 
    def move(self):
        print("I glide along the floor")

class baby(animal): 
    def move(self):
        print("I can crawl")

class bird(animal): 
    def move(self):
        print("I can fly")

class dolphin(animal): 
    def move(self):
        print("I can swim")

obj1 = human()
obj1.move()

obj2 = snake()
obj2.move()

obj3 = baby()
obj3.move()

obj4 = bird()
obj4.move()

obj5 = dolphin()
obj5.move()

