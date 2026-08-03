class account_class: 
    def __init__(self,owner,pin):
        self.owner = owner
        self.__pin = pin

    def show_pin_status(self): 
        print(f"Account Owner: {self.owner}")
        print("Pin is safely stored inside the class")

    def check_pin(self): 
         entered_pin = 0
         while True:
            try:
                entered_pin = int(input(f"Hello {self.owner} enter your desired PIN (4 digits or type 'done' to exit): ").strip().lower())

                if entered_pin == 'done':
                    break

                if len(str(entered_pin)) > 4:
                    print("too long try again")

                elif len(str(entered_pin)) < 4 :
                    print("Too short try again")

                else:
                    break

                if entered_pin == self.__pin:
                    print("Access Granted")
                    break

                else: 
                    print("Access denied")
                    break

            except ValueError:
                print("Error: invalid input")

        
        

    def set_pin(self):
        while True:
            try:
                new_pin = int(input(f"Hello {self.owner} enter your desired PIN (4 digits or type 'done' to exit): ").strip().lower())

                if new_pin == 'done':
                    break

                if len(str(new_pin)) > 4:
                    print("too long try again")

                elif len(str(new_pin)) < 4 :
                    print("Too short try again")

                else:
                    break

            except ValueError:
                print("Error: invalid input")


    def __str__(self):
        return(f"Owner: {self.owner}")
            
        self.__pin = new_pin

my_account = account_class("Yuvraj", 9999)

print(my_account)

my_account.show_pin_status()

my_account.check_pin()

my_account.set_pin()
        