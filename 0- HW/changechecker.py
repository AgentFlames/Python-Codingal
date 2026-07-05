def change(): 
    while True:
        amountpayed = int(input("How much did you pay?:  "))
        amountowed = int(input("How much did you owe?: "))

        if amountowed > amountpayed:
            print("Error: You haven't paid enough money yet.")
            
        elif amountowed <= 0 or amountpayed <= 0 : 
            print("amount owed cant be in the negatives")
        
        else:
            return amountpayed - amountowed
    

change_given = change()
print(f"You get €{change_given} back")