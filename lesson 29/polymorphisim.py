class Pakistan: 
    def capital(self):
        print("The capital of pakistan is islamabad")

    def laungage(self):
        print("Urdu is the main laungage of pakistan ")

    def type(self):
        print("Pakistan is a devolping country")

class Ireland: 
    def capital(self):
        print("The capital of Ireland is Dublin")

    def laungage(self):
        print("English is the main laungage of Ireland ")

    def type(self):
        print("Ireland is a developed country")


obj1 = Pakistan()
obj2 = Ireland()

for i in (obj1,obj2): 
    print("-" *20)
    i.capital()
    i.laungage()
    i.type()