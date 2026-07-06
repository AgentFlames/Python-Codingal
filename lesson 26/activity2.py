class employee ():

    def __init__(self):
        print("Employee created")

    def __del__(self):
        print("Employee deleted")


def create_obj():
    print("making object .....")
    obj = employee()
    print("Function ended")
    return obj

print("Calling create_obj() function")
obj1 =  create_obj()
print("Program finsished")