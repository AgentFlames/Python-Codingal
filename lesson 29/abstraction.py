from abc import ABC,abstractmethod

class absclass(ABC): 
    def print(self,x):
        print(f"Passed value: {x}")


    @abstractmethod

    def task(self): 
        print("We are inside absclass task")


class new_class(absclass):
    def task(self): 
        print("we are inside new_class task")


obj1 = new_class()

obj1.task()
obj1.print("hello world")