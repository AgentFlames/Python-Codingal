class dailyMessage: 
    def __init__(self,string=""):
        self.string=string

    def get_message(self): 
        self.string = input("Enter Your Message")

    def print_message(self):
        print(self.string.upper())

class Helpersession: 
    def __init__(self):
        print("Session Started") 

    def __del__(self): 
        print("session ended")

def create_session(): 
    return Helpersession()

class PairFinder: 

    def __init__(self,results=set()):
        self.results = results
        
    def find_pair(self): 
        target_value = int(input("enter a target value"))
        data = []
        self.results = set()
        for i in range(target_value): 
            data.append(i)
            i+=1

        for i,a in enumerate(data):
            for j,b in enumerate(data[i+1:]):
                if a+b == target_value: 
                    if a>b: 
                        self.results.add((b,a))
                    else: 
                        self.results.add((a,b))

        print(self.results)
        print(f"it has {len(self.results)} pairs")
                

daily_text = dailyMessage()
daily_text.get_message()
daily_text.print_message()

pair_finder = PairFinder()
pair_finder.find_pair()