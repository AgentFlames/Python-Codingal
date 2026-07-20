class Myclass: 
    __privatenum = 12
    num = 20

    def __privfunc(self): 
        print("This function is private")

    def print_priv(self): 
        print(f"Private number is {Myclass.__privatenum}")

obj = Myclass()
print(obj.num)
# print(obj.__privatenum)
obj.print_priv()