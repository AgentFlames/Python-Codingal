def shutdown():
    while True:
        try:
            conf = input("would you like to shutdown(yes/no)? : ").lower().strip()
            if conf == "yes":
                print("System shutting down.. ")
                exit()
            
            elif conf == "no":
                print("System shutdown aborted")
                return 0 

            else:
                print("sorry")

        except ValueError:
            print("sorry")

shutdown()