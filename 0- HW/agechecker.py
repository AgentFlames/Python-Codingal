while True:
    try: 
        num = int(input("Enter your age: "))
        if num %2 == 0:
            print("Your age is even ")

        else:
            print("Your age is odd")
            
    except ValueError: 
        print("ERROR: Invalid Input")