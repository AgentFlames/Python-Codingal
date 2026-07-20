class comp:
    def __init__(self):
        self.__maxprice = 900

    def sell(self): 
        print(f"Price of computer : {self.__maxprice}") 

    def set_price(self,price): 
        self.__maxprice = price


comp1 = comp()
comp1.sell()
comp1.__maxprice = 1000
comp1.sell()
comp1.set_price(1000)
comp1.sell()


    