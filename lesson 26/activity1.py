class upper_string():

    def __init__(self):
        self.str1 = ""

    def get_string(self):
        self.str1 = input("Enter a string: ")

    def print_str(self):
        print(f"the upper case of your string is : {self.str1.upper()}")

ob1 = upper_string()
ob1.get_string()
ob1.print_str()