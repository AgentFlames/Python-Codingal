import math

while True:
    print("-" * 20 , " math helper ", "-" * 20)
    dec = input("Choose Option (1.Sin , 2.Cos , 3.Tan ) or type 'done' to exit: ").lower().strip()
    
    if dec == "done": 
        print("Goodbye!")
        break

    if dec in ["1" , "2" , "3"]:
        try: 
            deg_val = float(input("Enter angle in degrees: "))
            deg_rad = math.radians(deg_val)

            if dec == "1":
                print(f"sin({deg_val}°) = {math.sin(deg_rad):.4f}")
            
            elif dec == "2":
                print(f"cos({deg_val}°) = {math.cos(deg_rad):.4f}")

            elif dec == "2":
                print(f"tan({deg_val}°) = {math.tan(deg_rad):.4f}")
       
        except ValueError:
            print("Error: Invalid Input")


    else: 
        print("Error: Enter either 1,2 or 3 please")